import sqlite3
import os.path
import sys


print('###############################')
print('path:'+os.getcwd())
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
            menu(c,conn)
            
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
        c.execute(check,[(username)])
        if c.fetchone():
            print('This email has already been registered!')
        else:
            new = ('''INSERT INTO members VALUES(?,'','',?)''')
            c.execute(new,[(username),(password)])
            conn.commit()
            print('You have successfully signed up!')
            return False

def logout(c,conn):
    print('FAREWELL')
    conn.close()
    main()

def close(c,conn):
    print('The program is closing...')
    print('Bye')
    conn.close()





#def OfferRide():
    #break

def SerchRide(c,conn):
    location_keyword = []
    for i in range(0,3):
        lkeyword = input("Please enter 1-3 location keywords: ").lower()
        location_keyword.append(lkeyword)
    retrieve = ('''SELECT * FROM rides WHERE src LIKE ''
                   
                ''')
    c.execute(retrieve,[(location_keyword[0])])
    for i in c.fetchall():
        print(i)
    
    
    
    
    print([(location_keyword[0])])
    



    
    
    
    
    
    
    
    
    
    
    
    

#def BookOrCancel():
    #break

#def PostRequests():
    #break

#def SerchAndDelete():
    #break
   
def menu(c,conn):
    print('1.Offer a ride')
    print('2.Search for rides')
    print('3.Book members or cancel bookings.')
    print('4.Post ride requests')
    print('5.Search and delete ride requests')
    print('6.Logout')
    print('7.Exit the program')
    task = input('What task would you like to perform(1-6):')
    if task == '1':
        OfferRide(c,conn)
        
    elif task == '2':
        SerchRide(c,conn)
        
    elif task == '3':
        BookOrCancel()
        
    elif task == '4':
        PostRequests()
        
    elif task == '5':
        SerchAndDelete()
    
    elif task == '6':
        logout(c,conn)
    
    elif task == '7':
        close(c,conn)
        
    
    

    

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


