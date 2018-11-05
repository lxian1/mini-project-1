import sqlite3
import os.path
import sys

def OfferRide(c, conn, username):  # The UI for when someone is inputting a ride.
    print("Please provide your ride information")
    ridedate = input("Ride Date (YYYY-MM-DD):")
    seats = input("How many seats will be offered?: ")
    if not assertInt(seats):
        return 0

    price = input("What is the price per seat?: $")
    if not assertInt(seats):
        return 0
    price = int(price)
    if price <= 0:
        print("Value must be positive")
        return 0

    lugdesc = input("Enter a description for the luggage:")

    src = input("Enter the source location (lcode, or keyword):")
    srclcode = HandleLocation(c, src)
    if not srclcode:
        return 0
    dst = input("Enter the destination location (lcode, or keyword):")
    dstlcode = HandleLocation(c, dst)
    if not dstlcode:
        return 0
    cno = input("Input Car number, or leave blank:")
    #if a value for cno was entered, check if the car belongs to them:
    if cno:
        c.execute('''SELECT cno 
                     FROM cars WHERE
                     owner = ? AND
                     cno = ?''', (username,cno))
        rows = c.fetchall()
        if(not len(rows) > 0):
            print("Car not found, or is not under your ownership.")
            return 0

    c.execute('''SELECT max(rno)
                 FROM rides''')
    rno = c.fetchone()[0] + 1

    c.execute('''INSERT INTO rides(rno, price, rdate, seats, lugDesc, src, dst, driver, cno)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (rno, price, ridedate, seats, lugdesc, srclcode, dstlcode, username, cno))
    conn.commit()
    print("Your ride has been created.")
    input("Press enter to continue...")
    return 1


def assertInt(value):  # Returns 1 if a valid integer was used.
    try:
        int(value)
    except ValueError:
        print("Value was not an integer amount!")
        return 0
    return 1


# This function handles whether a lcode entered is valid
# or helps find a city based off of a keyword.
# returns an lcode if we were able to find a location
# returns 0 if no location was found
def HandleLocation(c, code):
    c.execute('''SELECT *
                FROM locations WHERE
                lcode = ?''', (code,))

    rows = c.fetchall()
    if len(rows) == 1:  # If there is only one location matching the string
        rows = rows[0]
        city, prov, address = rows[1], rows[2], rows[3]
        print("Location set to: %s, %s, %s" % (address, city, prov))
        return rows[0] # Return lcode
    else:
        code = ("%" + code + "%")
        c.execute("SELECT * FROM locations WHERE address LIKE ? OR prov LIKE ? OR city LIKE ?", (code, code, code))
        rows = c.fetchall()
        if len(rows) == 0:
            print("No locations found")
            return 0
        row = Scroll5(rows, """"Multiple locations found, please select from below.\n
       Number, Lcode, City, Province, Address""")
        return row[0] # Return lcode


# This function will take in a list of rows (List of tuples)
# And scrolls through it, 5 at a time based off of user input.
# Returns the row the user selects
def Scroll5(rows, title):
    current = 0
    while (True):
        print("\n")
        print(title)
        for i in range(current, current + 5):
            if i > len(rows) - 1:
                continue
            print("%d." % (i + 1), rows[i])

        validinput = False
        option = ""
        while (not validinput):
            print("")
            if current + 5 > len(rows) - 1:
                option = input("Select a number from above, or 'prev' to see previous options: ")
                if option == "prev":
                    validinput = True
            elif current == 0:
                option = input("Select a number from above, or input 'next' for more options: ")
                if option == "next":
                    validinput = True
            else:
                option = input("Select a number from above, or input 'prev or 'next' to see previous or more options: ")
                if option == "next" or option == "prev":
                    validinput = True

            if not validinput:
                try:
                    numoption = int(option)
                except ValueError:
                    print("Invalid input")
                else:
                    if 1 <= numoption and numoption <= len(rows):
                        return rows[int(option) - 1]
                    else:
                        print("Invalid option number, out of bounds.")
        if option == "next":
            current += 5
        elif option == "prev":
            current -= 5

def BookOrCancel(c,conn,username):
    while(True):
        print("\nYour bookings:")
        c.execute('''SELECT bno, email, rides.seats, cost, pickup, dropoff 
                     FROM bookings, rides WHERE
                     bookings.rno = rides.rno AND
                     rides.driver = ?''',(username,))
        rows = c.fetchall()
        for row in rows:
            print("%s: email: %s, seats: %s, cost: $%s, pickup: %s, dropoff: %s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
        print("\n1. Create a new booking")
        print("2. Cancel a booking\n")
        choice = input("Please enter an option number, or 'exit': ")

        if(choice[0] == "1"): #Create a new booking
            c.execute('''SELECT * FROM(
                         SELECT rides.rno, rides.price, rides.rdate, 
                         rides.seats, rides.lugDesc, rides.src, rides.dst, 
                         rides.driver, rides.cno, CAST(rides.seats - total(bookings.seats) AS INT) FROM
                         rides LEFT OUTER JOIN bookings ON
                         rides.rno = bookings.rno
                         GROUP BY rides.rno)
                         WHERE driver = ?''', (username,))
            rows = c.fetchall()
            if len(rows) == 0:
                print("No rides found")
                input("Press enter to continue...\n")
                break

            row = Scroll5(rows, "Select one of your rides to book\nrno, price, rdate, seats, lugDesc, src, dst, driver, cno, seats available")
            rno = row[0]
            member = input("Enter the email of the member you would like to book: ")
            seats = int(input("Enter the number of seats to book: "))

            contin = True
            if seats > row[9]: # Overbooking detection
                while (True):
                    choice = input("Warning: this ride will be overbooked. Continue? (Y/N): ").upper()
                    if choice[0] == "N":
                        contin = False
                        break
                    elif choice[0] == "Y":
                        contin = True
                        break
            if not contin:
                continue

            costper = int(input("Enter the cost per seat: $"))
            pickup = input("Enter the pickup location code: ")
            dropoff = input("Enter the dropoff location code: ")
            cost = costper * seats

            c.execute('''SELECT max(bno) + 1 FROM
                         bookings''')
            bno = c.fetchone()[0]
            c.execute('''INSERT INTO bookings
                         VALUES(?, ?, ?, ?, ?, ?, ?)''', (bno, member, rno, cost, seats, pickup, dropoff))
            message = "Booking created: %s, with %s, from %s to %s" % (bno, username, pickup, dropoff)
            c.execute('''INSERT INTO inbox
                         VALUES(?, datetime("now"), NULL, ?, ?, "n")''', (member, message, rno))

            print("Booking created successfully")
            input("Press enter to continue...")

        elif(choice[0] == "2"): #Cancel a booking
            choice = input("Enter the booking number you would like to cancel: ")
            c.execute('''SELECT bno, driver, rdate, src, dst, email, rides.rno FROM 
                         bookings, rides WHERE
                         bookings.rno = rides.rno AND
                         bno = ? AND 
                         driver = ?''', (choice, username))
            rows = c.fetchall()

            if(len(rows) == 1):
                c.execute('''DELETE FROM
                             bookings WHERE
                             bno = ?''', (choice,))
                rows = rows[0]
                message = "Booking cancelled: %s, with %s, at %s from pickup %s to dropoff %s" % (rows[0], rows[1], rows[2], rows[3], rows[4])
                c.execute('''INSERT INTO inbox
                             VALUES(?, datetime("now"), NULL, ?, ?, "n")''', (rows[5], message, rows[6]))
            else:
                print("Failed to delete booking: invalid number, or you do not have permission")
                input("Press enter to continue...")

        elif(choice == "exit"):
            return 1

        conn.commit()

def PostRequests():
    pass

def SearchAndDelete(c, conn, username):
    while(True):
        print("")
        print("Your ride requests:\n")
        c.execute('''SELECT * FROM
                     requests WHERE
                     email = ?''', (username,))
        rows = c.fetchall()
        if len(rows) == 0:
            print("(no requests found)")
        else:
            print("rid, email, rdate, pickup, dropoff, amount")
            i = 1
            for row in rows:
                print("%d:" % i,row)
                i += 1

        print("")
        print("1. Search for a request")
        if len(rows) != 0:
            print("2. Delete a ride request")
        print("")
        choice = input("Please enter an option number, or 'exit': ")
        if choice == "1":
            code = (input("Please enter a location code, or city name: ")).capitalize()
            c.execute('''SELECT DISTINCT rid, email, rdate, pickup, dropoff, amount
                         FROM requests, locations WHERE
                         requests.pickup = locations.lcode AND
                         locations.lcode LIKE ? OR
                         locations.city LIKE ?''', (code,code))
            rows = c.fetchall()
            if len(rows) == 0:
                print("No locations found.")
                input("Press enter to continue...\n")
                continue

            email = Scroll5(rows, "Select a request to message the creator")[1]
            message = input("Type a message to send: ")
            c.execute('''INSERT INTO inbox(email,msgTimestamp,sender, content, rno, seen)
                         VALUES(?, datetime("now"), ?, ?, NULL, "n")''', (email, username, message))
            conn.commit()
            print("Message sent")

        elif choice == "2" and len(rows) != 0:
            selection = int(input("Please enter the index number above of the request you would like to delete: "))
            if selection < 1 or selection > len(rows):
                print("Invalid index")
                input("Press enter to continue...\n")
                continue
            c.execute('''DELETE FROM requests WHERE
                         rid = ?''', (rows[selection - 1][0],))
            conn.commit()
        elif choice == "exit":
            print("")
            return 1
        else:
            print("Invalid input")
            input("Press enter to continue...\n")

def SearchRide(c,conn,username):

    words = input("Please enter 1-3 keywords, separated by commas. ex: a,b,c: ")
    wordlist = words.split(",")
    keywords = []
    for i in range(3):
        if i > len(wordlist) - 1:
            keywords.append("")
        else:
            keywords.append(wordlist[i])

    c.execute('''SELECT DISTINCT * FROM(
                 SELECT * FROM rides 
                 LEFT OUTER JOIN locations ON locations.lcode = rides.src
                 UNION
                 SELECT * FROM rides
                 LEFT OUTER JOIN locations ON locations.lcode = rides.dst
                 UNION
                 SELECT * FROM enroute
                 LEFT OUTER JOIN rides USING(rno)
                 LEFT OUTER JOIN locations USING(lcode)) WHERE 
                 :k1 = lcode OR city LIKE :k1 OR prov LIKE :k1 OR address LIKE :k1 OR
                 :k2 = lcode OR city LIKE :k2 OR prov LIKE :k2 OR address LIKE :k2 OR
                 :k3 = lcode OR city LIKE :k3 OR prov LIKE :k3 OR address LIKE :k3
                 GROUP BY rno                   
                 ''',{"k1":"%" + keywords[0] + "%","k2":"%" + keywords[1] + "%","k3":"%" + keywords[2] + "%"})

    rows = c.fetchall()

    if len(rows) == 0:
        print("No results found")
        input("Press enter to continue...\n")
        return True

    row = Scroll5(rows,"Here are the results: ")
    print('You have selected the following ride: ')
    print(row)
    email = row[7]
    content = 'I want to book a seat on your ride.'
    rno = row[0]
    seen = 'n'
    sender = username
    message = ('''INSERT INTO inbox
                  VALUES(?,DateTime('now'),?,?,?,?)
               ''')
    c.execute(message,[(email),(sender),(content),(rno),(seen)])
    conn.commit()
    print('A message has been sent to the driver.')
    input("Press enter to continue...\n")

def menu(c, conn, username):
    while(True):
        print('1.Offer a ride')
        print('2.Search for rides')
        print('3.Book members or cancel bookings.')
        print('4.Post ride requests')
        print('5.Search and delete ride requests')
        print('6.Logout')
        print('7.Exit the program')
        task = input('What task would you like to perform(1-6):')
        if task == '1':
            OfferRide(c, conn, username)

        elif task == '2':
            SearchRide(c,conn,username)

        elif task == '3':
            BookOrCancel(c, conn, username)

        elif task == '4':
            PostRequests()

        elif task == '5':
            SearchAndDelete(c, conn, username)

        elif task == '6':
            print("Logging out. Farewell!")
            return False

        elif task == '7':
            return True

def login():
    while True:
        username = input('Please enter your username(email): ')
        if username == 'exit':
            sys.exit('The program is closed')
        password = input('Please enter your password(integer): ')
        if password == 'exit':
            sys.exit('The program is closed')
        file = sys.argv[1]
        conn = sqlite3.connect('./%s' % file)
        c = conn.cursor()
        check = ('''SELECT * 
                    FROM members 
                    WHERE email = ? 
                    AND pwd = ?''')
        c.execute(check, [(username), (password)])
        result = c.fetchone()
        if result:
            print('Welcome back!\n')
            message = ('''SELECT content
                          From inbox
                          Where email = ? AND
                          seen = "n"''')
            c.execute(message, [username])
            print('Unread messages: ')
            rows = c.fetchall()
            if len(rows) == 0:
                print("(You have no new messages)")
            for email in rows:
                print(email)
            update_seen = ('''UPDATE inbox
                              SET seen = 'y'
                              WHERE email = ?''')
            c.execute(update_seen, [username])
            conn.commit()
            print("")
            # Start the menu:
            if menu(c, conn, username): # If we get back a true value, terminate the program. Propagate up to main
                conn.close()
                return True

            return False
        else:
            print('Invalid account!')
            print('Try Again!')


def register():
    while True:
        print("")
        print("Now registering a new account. Type 'exit' to cancel")
        username = input('Please provide your username(email): ')
        if username == 'exit':
            return True
        password = input('Please create your password(integer): ')
        if password == 'exit':
            return True
        file = sys.argv[1]
        conn = sqlite3.connect('./%s' % file)
        c = conn.cursor()
        check = ('''SELECT * 
                    FROM members 
                    WHERE email = ? ''')
        c.execute(check, [(username)])
        if c.fetchone():
            print('This email has already been registered!')
        else:
            new = ('''INSERT INTO members VALUES(?,'','',?)''')
            c.execute(new, [(username), (password)])
            conn.commit()
            print('You have successfully signed up!')
            return False

def logout(c, conn):
    print('FAREWELL')
    conn.close()

def main():
    while(True):
        print("Program Login\n")
        print("1. Login")
        print("2. Register\n")

        membership = input("Please enter the number corresponding to your selection, or 'exit' to terminate the program: ").upper()
        if membership == '1':
            if login():  # If login returns a true value, then we should terminate the program.
                break
        elif membership == '2':
            if register():  # If register returns a true value, then an account was not registered. Clear menu
                continue
            if login():
                break
        elif membership == 'EXIT':
            break

    return 0
main()