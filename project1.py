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
            print('This eamil has already been registered!')
        else:
            new = ('''INSERT INTO members VALUES(?,'','',?)''')
            c.execute(new,[(username),(password)])
            conn.commit()
            print('You have successfully signed up!')
            return False
  
            
    

def main():
    membership = input('Do you have an account?(Y/N):')
    if membership == 'Y':
        login()
    else:
        register()
        login()
    
    
main()


