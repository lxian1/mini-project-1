import sqlite3
import os.path
import sys

print('###############################')
print('path:' + os.getcwd())
print('###############################')


def login():
    while True:
        username = input('Please enter your username(email): ')
        if username == 'exit':
            sys.exit('The program is closed')
        password = input('Please enter your password(integer): ')
        if password == 'exit':
            sys.exit('The program is closed')
        conn = sqlite3.connect('./project1.db')
        c = conn.cursor()
        check = ('''SELECT * 
                    FROM members 
                    WHERE email = ? 
                    AND pwd = ?''')
        c.execute(check, [(username), (password)])
        result = c.fetchone()
        if result:
            print('Welcome back!')
            print('Your personal information: ')
            print(result)
            message = ('''SELECT content
                          From inbox
                          Where email = ?''')
            c.execute(message, [username])
            print('#######################')
            print('Your unread message: ')
            print(c.fetchone())
            update_seen = ('''UPDATE inbox
                              SET seen = 'y'
                              WHERE email = ?''')
            c.execute(update_seen, [username])
            conn.commit()
            menu(c, conn, username)

            return False
        else:
            print('Invalid account!')
            print('Try Again!')


def register():
    while True:
        username = input('Please provide your username(email): ')
        if username == 'exit':
            sys.exit('The program is closed')
        password = input('Please create your password(integer): ')
        if password == 'exit':
            sys.exit('The program is closed')
        conn = sqlite3.connect('./project1.db')
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
    main()


def close(c, conn):
    print('The program is closing...')
    print('Bye')
    conn.close()



def OfferRide(c, conn, username):  # The UI for when someone is inputting a ride.
    print("Please provide your ride information")

    ridedate = input("Ride Date (YYYY-MM-DD):")  # TODO: Validate date

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
    dst = input("Enter the destination location (lcode, or keyword):")
    dstlcode = HandleLocation(c, dst)
    if(not srclcode or not dstlcode):
        print("Invalid src or dst")

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
    c.execute('''SELECT max(rno)
                 FROM rides''')
    rno = c.fetchone()[0] + 1


    print((rno, price, ridedate, seats, lugdesc, srclcode, dstlcode, username, cno))
    c.execute('''INSERT INTO rides(rno, price, rdate, seats, lugDesc, src, dst, driver, cno)
                 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (rno, price, ridedate, seats, lugdesc, srclcode, dstlcode, username, cno))
    conn.commit()
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
        row = Scroll5(rows, """"Multiple locations found, please select from below.\n
       Number, Lcode, City, Province, Address""")
        return row[0] # Return lcode


# This function will take in a list of rows (List of tuples)
# And scrolls through it, 5 at a time based off of user input.
# Returns the row the user selects
def Scroll5(rows, title):
    current = 0
    while (True):
        print(title)
        for i in range(current, current + 5):
            if i > len(rows) - 1:
                print("")
                continue
            print(i + 1, rows[i])

        validinput = False
        option = ""
        while (not validinput):
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

def ValidDate():  # TODO This function will check if the date someone enters is valid
    pass

# def BookOrCancel():
# break

# def PostRequests():
# break

# def SerchAndDelete():
# break

def menu(c, conn, username):
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
        SerchRide(c, conn)

    elif task == '3':
        BookOrCancel()

    elif task == '4':
        PostRequests()

    elif task == '5':
        SerchAndDelete()

    elif task == '6':
        logout(c, conn)

    elif task == '7':
        close(c, conn)


def main():
    print('You can exit anytime by input "exit"')
    membership = input('Do you have an account?(Y/N):').upper()
    if membership == 'Y':
        login()
    elif membership == 'N':
        register()
        login()
    elif membership == 'EXIT':
        sys.exit('The program is closed')

main()



