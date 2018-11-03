import sqlite3
import os.path

print('###############################')
print('path:'+os.getcwd())
print('###############################')

def login():
    while True:
        username = input('Please enter your username(email): ')
        password = input('Please enter your password(integer): ')
        conn = sqlite3.connect('./project1.db')
        c = conn.cursor()
        check = ('''SELECT * 
                    FROM members 
                    WHERE email = ? 
                    AND pwd = ?''')
        c.execute(check,[(username),(password)])
        result = c.fetchone()
        if result:
            print('Welcome back!')
            print('Your personal information: ')
            print(result)
            message = ('''SELECT content
                          From inbox
                          Where email = ?''')
            c.execute(message,[username])
            print('#######################')
            print('Your unread message: ')
            print(c.fetchone())
            update_seen = ('''UPDATE inbox
                         SET seen = 'y'
                         WHERE email = ?''')
            c.execute(update_seen,[username])
            conn.commit()

            return False
        else:
            print('Invalid account!')
            print('Try Again!')

def register():
    while True:
        username = input('Please provide your username(email): ')
        password = input('Please create your password(integer): ')
        conn = sqlite3.connect('./project1.db')
        c = conn.cursor()
        check = ('''SELECT * 
                    FROM members 
                    WHERE email = ? ''')
        c.execute(check,[(username)])
        if c.fetchone():
            print('This email has already been registered!')
        else:
            new = ('''INSERT INTO members VALUES(?,'','',?)''')
            c.execute(new,[(username),(password)])
            conn.commit()
            print('You have successfully signed up!')
            return False
  


def OfferRide(c, conn, username): # The UI for when someone is inputting a ride.
    print("Please provide your ride information")
    ridedate = input("Ride Date (YYYY-MM-DD):") # TODO: Validate date
    seats = input("How many seats will be offered?: ")
    try:
        int(seats)
    except ValueError:
        print("Value was not an integer amount!")
        return 0
    price = input("What is the price per seat?: $")
    try:
        int(seats)
    except ValueError:
        print("Value was not an integer amount!")
        return 0
    lugdesc = input("Enter a description for the luggage:")
    src = input("Enter the source location (lcode, or keyword):")
    HandleLocation(c, src)
    dst = input("Enter the destination location (lcode, or keyword):")
    HandleLocation(c, dst)

# This function handles whether a lcode entered is valid
# or helps find a city based off of a keyword.
# returns an lcode if we were able to find a location
# returns 0 if no location was found
def HandleLocation(c, code):
    c.execute("""SELECT *
                 FROM locations WHERE
                 lcode = ?""", code)

    rows = c.fetchall()
    if len(rows) == 1: # If there is only one location matching the string
        city, prov, address = rows[1],rows[2],rows[3]
        print("Location set to: %s, %s, %s" % (address, prov, city))
    else:
        check = c.execute('SELECT * FROM locations WHERE address LIKE ? OR prov LIKE ? OR city LIKE ?', ('%' + code + '%'))

        rows = c.fetchall()
        row = Scroll5(rows,""""Multiple locations found, please select from below.\n
        Number, Lcode, City, Province, Address""")
        return row[0]


# This function will take in a list of rows (List of tuples)
# And scrolls through it, 5 at a time based off of user input.
# Returns the row the user selects
def Scroll5(rows, title):
    current = 0
    while(True):
        print(title)
        for i in range(current, current+5):
            if i > len(rows) - 1:
                print("")
                continue
            print(i + 1,rows[i])

        validinput = False
        option = ""
        while(not validinput):
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
                        return rows[int(option)]
                    else:
                        print("Invalid option number, out of bounds.")
        if option == "next":
            current += 5
        elif option == "prev":
            current -= 5







def ValidDate(): # TODO This function will check if the date someone enters is valid
    pass




def main():
    membership = input('Do you have an account?(Y/N):').upper()
    if membership == 'Y':
        login()
    else:
        register()
        login()

main()