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
            menu()
            
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
            print('This eamil has already been registered!')
        else:
            new = ('''INSERT INTO members VALUES(?,'','',?)''')
            c.execute(new,[(username),(password)])
            conn.commit()
            print('You have successfully signed up!')
            return False

#def logout():
    #break

#def OfferRide():
    #break

#def SerchRide():
    #break

#def BookOrCancel():
    #break

#def PostRequests():
    #break

#def SerchAndDelete():
    #break
   
def menu():
    print('1.Offer a ride')
    print('2.Search for rides')
    print('3.Book members or cancel bookings.')
    print('4.Post ride requests')
    print('5.Search and delete ride requests')
    print('6.logout')
    task = input('What task would you like to perform(1-5):')
    if task == '1':
        OfferRide()
        
    elif task == '2':
        SerchRide()
        
    elif task == '3':
        BookOrCancel()
        
    elif task == '4':
        PostRequests()
        
    elif task == '5':
        SerchAndDelete()
    
    elif task == '6':
        logout()
        
    
    

    

def main():
    membership = input('Do you have an account?(Y/N):')
    if membership == 'Y':
        login()
    else:
        register()
        login()
    
    
main()


