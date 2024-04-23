#Importing Modules
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import sqlite3

#Connecting Employee Database
conn = sqlite3.connect('accounts.db')

#Creating Employee Database cursor
cursor = conn.cursor()

# Create a table to store the user credentials
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                     ( username text, password text, account_type text)''')

#Insert Values
cursor.execute('''INSERT INTO users VALUES ('testuser1', 'test1', 'Type 1')''')

#Insert Values
cursor.execute('''INSERT INTO users VALUES ('testuser2', 'test2', 'Type 2')''')

#Creating Web Function
class web:

    #Creating the Initial Web Page Function
    def __init__(page):
        
        #Creating Root File and Window
        page.root = tk.Tk()

        #Creating Frame for widgets
        page.frame = tk.Frame(page.root)


        #Implementing the different columns within the frame
        page.frame.columnconfigure(0, weight=1)
        page.frame.columnconfigure(1, weight=1)
        page.frame.columnconfigure(2, weight=1)
        page.frame.columnconfigure(3, weight=1)
        page.frame.columnconfigure(4, weight=1)
        page.frame.columnconfigure(5, weight=1)
        page.frame.columnconfigure(6, weight=1)

        #Setting the size of the window and also the title
        page.root.geometry("1000x650")
        page.root.title("Wye Camping & Leisure")
        
        #Setting Username and Variable Passwords
        username = StringVar()
        password = StringVar()

        #Title on Webpage
        page.label1 = tk.Label(page.root, text="Wye Camping & Leisure Online Store", font=('Arial', 18))
        page.label1.grid(row=1, column=1, padx=20, pady=20)

        #Welcome Message
        page.label2 = tk.Label(page.root, text="Welcome to the Wye Camping & Leisure online shop and business application.", font=('Arial', 14))
        page.label2.grid(row=2, column=1, padx=10, pady=10)

        #Username Text
        page.label3 = tk.Label(page.root, text="Username: ", font=('Arial', 14))
        page.label3.grid(row=4, column=1, padx=20, pady=20)

        #Username Entry Text Box
        username = tk.Entry(page.root, textvariable=username,  font=('Arial', 16))
        username.grid(row=5, column=1, padx=10, pady=10)
        #log_username = page.entrybox1.get().lower()

        #Password Text
        page.label4 = tk.Label(page.root, text="Password: ", font=('Arial', 14))
        page.label4.grid(row=6, column=1, padx=20, pady=20)

        #Password Entry Text Box
        passwrd = tk.Entry(page.root, textvariable=password, font=('Arial', 16))
        passwrd.grid(row=7, column=1, padx=10, pady=10)
        #log_pass = page.entrybox2.get().lower()

        #Account Type Select Box
        tk.Label(page.root, text='Account type:', font=('Arial', 16)).grid(row=8, column=1, padx=20, pady=20)
        account_type_var = tk.StringVar(page.root)
        account_type_user = tk.OptionMenu(page.root, account_type_var, 'Type 1', 'Type 2')
        account_type_user.grid(row=9, column=1)

        # Create a function to check the login credentials
        def check_login():
            # Connect to the database
            conn = sqlite3.connect('accounts.db')
            cursor = conn.cursor()
            
            # Check if the entered username and password are correct
            cursor.execute('''SELECT * FROM users WHERE username=? AND password=? AND account_type=?''', (username.get(), passwrd.get(), account_type_var.get()))
            result = cursor.fetchone()
            
            # If the query returns a result, the login is successful
            if result:
                new_page = tk.Toplevel(page.root)
                tk.Label(new_page, text='Login successful').grid(row=10, column=1)
            else:
                tk.Label(page.root, text='Invalid username or password').grid(row=10, column=1)
    
            # Close the connection
            conn.close()
            
        # Create a login button
        tk.Button(page.root, text='Login', font='Arial, 16', command=check_login).grid(row=9, column=0, pady=10)

        #Shop Page
        def shop(page):
            
            #Creating Shop Page
            #Creating New Window
            shop= Toplevel(page.root)
            shop.title("Shop Home Page")
            shop.geometry("700x500")

            #Creating the Frame for the Shop Window
            shop.frame = tk.Frame(shop)

            #Title on Customer Register Page
            shop.label1 = tk.Label(shop, text="Wye Camping & Leisure Shop", font=('Arial', 18))
            shop.label1.grid(row=0, column=1, padx=20, pady=20)

            #Implementing the different columns within the frame
            shop.frame.columnconfigure(0, weight=1)
            shop.frame.columnconfigure(1, weight=1)
            shop.frame.columnconfigure(2, weight=1)
            shop.frame.columnconfigure(3, weight=1)
            shop.frame.columnconfigure(4, weight=1)
            shop.frame.columnconfigure(5, weight=1)
            shop.frame.columnconfigure(6, weight=1)

            #Shop Web Page Mainloop
            shop.mainloop()

        #Employee Account Switch Function
        def employee(page):
            
            #Creating Employee Login Screen
            #Creating New Window
            empLogin= Toplevel(page.root)
            empLogin.title("Employee Login")
            empLogin.geometry("950x500")

            #Creating the Frame for the Employee Login Page
            empLogin.frame = tk.Frame(empLogin)

            #Title on Employee Login Page
            empLogin.label1 = tk.Label(empLogin, text="Wye Camping & Leisure Employee Login Page", font=('Arial', 18))
            empLogin.label1.grid(row=0, column=1, padx=20, pady=20)

            #Implementing the different columns within the frame
            empLogin.frame.columnconfigure(0, weight=1)
            empLogin.frame.columnconfigure(1, weight=1)
            empLogin.frame.columnconfigure(2, weight=1)
            empLogin.frame.columnconfigure(3, weight=1)
            empLogin.frame.columnconfigure(4, weight=1)
            empLogin.frame.columnconfigure(5, weight=1)
            empLogin.frame.columnconfigure(6, weight=1)

            #Employee Username Text
            empLogin.label2 = tk.Label(empLogin, text="Username: ", font=('Arial', 14))
            empLogin.label2.grid(row=2, column=1, padx=10, pady=10)

            #Employee Username Entry Text Box
            empLogin.entrybox1 = tk.Entry(empLogin, font=('Arial', 16))
            empLogin.entrybox1.grid(row=5, column=1, padx=10, pady=10)

            #Employee Password Text
            empLogin.label3 = tk.Label(empLogin, text="Password: ", font=('Arial', 14))
            empLogin.label3.grid(row=6, column=1, padx=20, pady=20)

            #Employee Password Entry Text Box
            empLogin.entrybox2 = tk.Entry(empLogin, font=('Arial', 16))
            empLogin.entrybox2.grid(row=7, column=1, padx=10, pady=10)
            
            #Employee Passkey Text
            empLogin.label4 = tk.Label(empLogin, text="Passkey: ", font=('Arial', 14))
            empLogin.label4.grid(row=8, column=1, padx=20, pady=20)

            #Employee Passkey Entry Text Box
            empLogin.entrybox3 = tk.Entry(empLogin, font=('Arial', 16))
            empLogin.entrybox3.grid(row=9, column=1, padx=10, pady=10)

            #Employee Login Button
            empLogin.logbtn = tk.Button(empLogin, text="Log in.", font=('Arial', 18), command=empLogin)
            empLogin.logbtn.grid(row=10, column=1, padx=10, pady=10)

            #Manage Employee Account Button
            empLogin.managebtn = tk.Button(empLogin, text="Manage Employee Accounts", font=('Arial', 18))
            empLogin.managebtn.grid(row=7, column=2, padx=10, pady=10)

            #Employee Login Page Mainloop
            empLogin.mainloop()
        
        #New Member Function Variable
        page.check_reg_state = tk.IntVar()

        #New Member Check Box
        page.check = tk.Checkbutton(page.root, text="New Member?", font=('Arial', 16), variable=page.check_reg_state)
        page.check.grid(row=4, column=2, padx=10, pady=10)

        #New Member Function
        def newMember():
            if page.check_reg_state.get() == 0:
                END
            else:
                newcustomer(page)

        #New Member Button
        page.newmembtn = tk.Button(page.root, text="New Member", font=('Arial', 18), command=newMember)
        page.newmembtn.grid(row=5, column=2, padx=10, pady=10)

        #Creating a Business Account Page
        def newcustomer(page):
            
            #Creating Registering Screen
            #Creating New Window
            custregister= Toplevel(page.root)
            custregister.title("New Customer Register Page")
            custregister.geometry("650x550")

            #Creating the Frame for the Customer Registering Pages Window
            custregister.frame = tk.Frame(custregister)

            #Title on Customer Register Page
            custregister.label1 = tk.Label(custregister, text="Wye Camping & Leisure New Customer Register Page", font=('Arial', 18))
            custregister.label1.grid(row=0, column=1, padx=20, pady=20)

            #Implementing the different columns within the frame
            custregister.frame.columnconfigure(0, weight=1)
            custregister.frame.columnconfigure(1, weight=1)
            custregister.frame.columnconfigure(2, weight=1)
            custregister.frame.columnconfigure(3, weight=1)
            custregister.frame.columnconfigure(4, weight=1)
            custregister.frame.columnconfigure(5, weight=1)
            custregister.frame.columnconfigure(6, weight=1)

            #Creating a Username Text
            custregister.label2 = tk.Label(custregister, text="Create a Username: ", font=('Arial', 14))
            custregister.label2.grid(row=2, column=1, padx=10, pady=10)

            #Register Username Entry Text Box
            custregister.entrybox1 = tk.Entry(custregister, font=('Arial', 16))
            custregister.entrybox1.grid(row=5, column=1, padx=10, pady=10)

            #Creating a Password Text
            custregister.label3 = tk.Label(custregister, text="Create a Password: ", font=('Arial', 14))
            custregister.label3.grid(row=6, column=1, padx=20, pady=20)

            #Register Password Entry Text Box
            custregister.entrybox2 = tk.Entry(custregister, font=('Arial', 16))
            custregister.entrybox2.grid(row=7, column=1, padx=10, pady=10)

            #Confirming Password Text
            custregister.label3 = tk.Label(custregister, text="Confirm Password: ", font=('Arial', 14))
            custregister.label3.grid(row=8, column=1, padx=20, pady=20)

            #Confirming Password Entry Text Box
            custregister.entrybox3 = tk.Entry(custregister, font=('Arial', 16))
            custregister.entrybox3.grid(row=9, column=1, padx=10, pady=10)

            #Register Button
            custregister.logbtn = tk.Button(custregister, text="Register", font=('Arial', 18))
            custregister.logbtn.grid(row=10, column=1, padx=10, pady=10)

            #Register Page Mainloop
            custregister.mainloop()

        #Creating Login Mainloop     
        page.root.mainloop()

#Commiting Web Function
web()

#Commiting Database Code
conn.commit()

#Close connection with the Employee database
conn.close()