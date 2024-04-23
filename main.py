import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.simpledialog import askstring
from tkinter import PhotoImage
import PIL
import io
from io import BytesIO
from PIL import *
from PIL import Image, ImageTk
import sqlite3
import uuid
import random
import string
import datetime

# Connect to the Accounts database
conn = sqlite3.connect('login.db')

#Creating a cursor to navigate the database
cursor = conn.cursor()

# Create a table to store the user credentials
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                     (user_id text PRIMARY KEY, username text, password text, account_type text, email text)''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()



# Connect to the Accounts database
conn = sqlite3.connect('contact.db')

#Creating a cursor to navigate the database
cursor = conn.cursor()

# Create a table to store the user credentials
cursor.execute('''CREATE TABLE IF NOT EXISTS info
                     (contact_id text PRIMARY KEY, email text, message text)''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()



# Connect to the image database
conn = sqlite3.connect('image.db')

#Creating a cursor to navigate the database
cursor = conn.cursor()

# Create a table to store the images the app will use
cursor.execute('''CREATE TABLE IF NOT EXISTS images
                     (image_id text PRIMARY KEY, image_data BLOB)''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()



# Connect to the Payment database
conn = sqlite3.connect('payment.db')

#Creating a cursor to navigate the database
cursor = conn.cursor()

# Create a table to store the payment credentials
cursor.execute('''CREATE TABLE IF NOT EXISTS payments
                     (payment_id text PRIMARY KEY, order_id, user_id, card_full_num, card_expiry, CVV, name_on_card, total_price)''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()



# Connect to the order database
conn = sqlite3.connect('shipping.db')

#Creating a cursor to navigate the database
cursor = conn.cursor()

# Create a table to store the order details
cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                     (order_id text PRIMARY KEY, user_id text, product_id INTEGER, payment_id text, total_price INTEGER, delivery_date text, purchase_date text, quantity INTEGER)''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()



# Connect to the Stockroom database
conn = sqlite3.connect('stockroom.db')

#Creating a cursor to navigate the database
cursor = conn.cursor()

# Create a table to store the product details
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                     (product_id INTEGER PRIMARY KEY, product_name text, quantity INTEGER, price INTEGER)''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()



# Create the login window
window = tk.Tk()
window.title('Login')
window.config(bg='#06CB30')


#Main Title on Login page
tk.Label(window, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#06CB30', fg='white').grid(row=0, column=0)

#Command
tk.Label(window, text='Please put your account details below.', font=("Arial", 16), bg='#06CB30', fg='white').grid(row=1, column=0)


#Getting Wye Camping Logo
conn = sqlite3.connect('image.db')
c = conn.cursor()

# Retrieving the image data from the database
c.execute("SELECT image_data FROM images WHERE image_id = ?", (1,))
image_data = c.fetchone()[0]

# Convert the image data to a Tkinter-compatible format
image = Image.open(BytesIO(image_data))
photo = ImageTk.PhotoImage(image)

#Putting the logo image into a label and displaying it on the website
logo = tk.Label(window, image=photo)
logo.grid(row=0, column=2)

#Commiting changes and closing connection
conn.commit()
c.close()


#Username Entry Box
tk.Label(window, text='Username:', bg='#06CB30', fg='white').grid(row=2, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=3, column=0, padx=15, pady=15)

#Password Entry Box
tk.Label(window, text='Password:', bg='#06CB30', fg='white').grid(row=4, column=0)
password_entry = tk.Entry(window, show='*')
password_entry.grid(row=5, column=0, padx=15, pady=15)

#Account Type Entry Box
tk.Label(window, text='Account type:', bg='#06CB30', fg='white').grid(row=6, column=0)
account_type_var = tk.StringVar(window)
account_type_user = tk.OptionMenu(window, account_type_var, 'Customer', 'Employee', 'Manager')
account_type_user.grid(row=7, column=0, padx=15, pady=15)

# Create a basket list to store the user's orders
basket = []

# Create a function to check the login credentials
def check_login():
    # Connect to the Accounts database
    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()
    
    # Check if any of the fields are empty
    if not username_entry.get():
        messagebox.showerror("Error", "Please enter your username.")
        return
    elif not password_entry.get():
        messagebox.showerror("Error", "Please enter your password.")
        return
    elif not account_type_var.get():
        messagebox.showerror("Error", "Please select your account type.")
        return

    #Check if the entered username and password are correct
    cursor.execute('''SELECT * FROM users WHERE username=? AND password=? AND account_type=?''', (username_entry.get(), password_entry.get(), account_type_var.get()))
    result = cursor.fetchone()

    #Account type based login system
    if result is not None:  # Check if result is not None before accessing its elements
        acc_type = result[3]
    else:
        messagebox.showerror("Error", "Invalid username or password.")
        return
    
    # If the query returns a result, the login is successful
    #Creating the Shop Web Page
    if acc_type == "Customer":
        
        #Creating a New Window for the Shop After Login
        shop_page = tk.Toplevel(window)
        shop_page.title("Shop Page")
        shop_page.geometry("1500x950")
        shop_page.config(bg='#06CB30')
        
        #Login Successful Message on Account Login page
        tk.Label(window, text='Login successful', bg='#06CB30', fg='white').grid(row=10, column=1)
        
        #Title of Shop Web Page
        tk.Label(shop_page, text="Wye Camping & Leisure Online Shop", font=("Arial", 18, "bold underline"), bg='#06CB30', fg='white').grid(row=0, column=1, padx=20, pady=20)
        
        #Message on Shop Web Page
        tk.Label(shop_page, text="Welcome to Wye Camping & Leisure where we sell quality camping equipment at affordable prices", font=("Arial", 16), bg='#06CB30', fg='white').grid(row=1, column=1, padx=20, pady=20)
        
        #Message on Shop Web Page
        tk.Label(shop_page, text="Here is the selection of items that we have on display today.", font=("Arial", 16), bg='#06CB30', fg='white').grid(row=5, column=1, padx=20, pady=20)

        #Getting Wye Camping Logo
        conn = sqlite3.connect('image.db')
        c = conn.cursor()

        # Retrieving the image data from the database
        c.execute("SELECT image_data FROM images WHERE image_id = ?", (1,))
        image_data = c.fetchone()[0]

        # Convert the image data to a Tkinter-compatible format
        image = Image.open(BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)

        #Putting the logo image into a label and displaying it on the website
        logo_shop = tk.Label(shop_page)
        logo_shop.image = photo
        logo_shop.configure(image=photo)
        logo_shop.grid(row=0, column=2)

        #Commiting changes and Closing Connection
        conn.commit()
        c.close()

        #Bungee Add to Basket Button
        bungee_basket = tk.Button(shop_page, text="Add to basket", command=lambda: bungee_add_basket()).grid(row=9, column=1, padx=20, pady=20)

        #Super Glue Add to Basket Button
        glue_basket = tk.Button(shop_page, text="Add to basket", command=lambda: glue_add_basket()).grid(row=9, column=0, padx=20, pady=20)

        #Awning Cleaner Add to Basket Button
        awning_cleaner_basket = tk.Button(shop_page, text="Add to basket", command=lambda: awning_cleaner_add_basket()).grid(row=9, column=2, padx=20, pady=20)

        #Super Glue Add to Basket Function
        def glue_add_basket():
            quantity_window = tk.Toplevel()
            quantity_window.title("Quantity")
            quantity_label = tk.Label(quantity_window, text="Enter quantity:")
            quantity_entry = tk.Entry(quantity_window)
            quantity_label.pack()
            quantity_entry.pack()

            def add_item():
                glue_quantity = quantity_entry.get()
                if glue_quantity.isnumeric():
                    basket.append(("Super Glue Twin Pack", int(glue_quantity), 4))
                    quantity_window.destroy()
            
            add_button = tk.Button(quantity_window, text="Add", command=add_item)
            add_button.pack()
        
        #Bungee Add to Basket Function
        def bungee_add_basket():
            quantity_window = tk.Toplevel()
            quantity_window.title("Quantity")
            quantity_label = tk.Label(quantity_window, text="Enter quantity:")
            quantity_entry = tk.Entry(quantity_window)
            quantity_label.pack()
            quantity_entry.pack()

            def add_item():
                bungee_quantity = quantity_entry.get()
                if bungee_quantity.isnumeric():
                    basket.append(("Bungee Ball Cord Loop", int(bungee_quantity), 10))
                    quantity_window.destroy()
            
            add_button = tk.Button(quantity_window, text="Add", command=add_item)
            add_button.pack()
        
        #Awning Cleaner Add to Basket Function
        def awning_cleaner_add_basket():
            quantity_window = tk.Toplevel()
            quantity_window.title("Quantity")
            quantity_label = tk.Label(quantity_window, text="Enter quantity:")
            quantity_entry = tk.Entry(quantity_window)
            quantity_label.pack()
            quantity_entry.pack()

            def add_item():
                awning_cleaner_quantity = quantity_entry.get()
                if awning_cleaner_quantity.isnumeric():
                    basket.append(("Cleaning Brush Awning Rail", int(awning_cleaner_quantity), 5))
                    quantity_window.destroy()
            
            add_button = tk.Button(quantity_window, text="Add", command=add_item)
            add_button.pack()
                
        #Super Glue Image + Info                            
        #Super Glue Title
        glue_label = tk.Label(shop_page, text="Super Glue Twin Pack", font=("Arial", 12), bg='#06CB30', fg='white').grid(row=6, column=0)
        glue_price = tk.Label(shop_page, text="£4", font=("Arial", 12), bg='#06CB30', fg='white').grid(row=7, column=0)
        with open("glue.jpg", "rb") as image_file: 
            image_data = image_file.read()      

        #Tkinter-compatible format
        image = Image.open(BytesIO(image_data))
        resized_image = image.resize((int(image.width/4), int(image.height/4)))
        photo = ImageTk.PhotoImage(resized_image)

        item1 = tk.Label(shop_page)
        item1.image = photo
        item1.configure(image=photo)
        item1.grid(row=8, column=0, padx=20, pady=20)



        #Bungee Cord Image + Info
        #Bungee Title
        tk.Label(shop_page, text="Bungee Ball Cord Loop", font=("Arial", 12), bg='#06CB30', fg='white').grid(row=6, column=1)
        bungee_price = tk.Label(shop_page, text="£10", font=("Arial", 12), bg='#06CB30', fg='white').grid(row=7, column=1)
        with open("bungee.jpg", "rb") as image_file: 
            bungee_image_data = image_file.read()      

        #Tkinter-compatible format
        bungee_image = Image.open(BytesIO(bungee_image_data))
        resized_bungee_image = bungee_image.resize((int(bungee_image.width/4), int(bungee_image.height/4)))
        bungee_photo = ImageTk.PhotoImage(resized_bungee_image)

        item2 = tk.Label(shop_page)
        item2.image = bungee_photo
        item2.configure(image=bungee_photo)
        item2.grid(row=8, column=1, padx=20, pady=20)



        #Awning Cleaner Image + Info
        #Awning Cleaner Title
        tk.Label(shop_page, text="Cleaning Brush Awning Rail", font=("Arial", 12), bg='#06CB30', fg='white').grid(row=6, column=2)
        awning_cleaner_price = tk.Label(shop_page, text="£5", font=("Arial", 12), bg='#06CB30', fg='white').grid(row=7, column=2)
        with open("awningcleaner.jpg", "rb") as image_file: 
            awning_cleaner_image_data = image_file.read()      

        #Tkinter-compatible format
        awning_cleaner_image = Image.open(BytesIO(awning_cleaner_image_data))
        resized_awning_cleaner_image = awning_cleaner_image.resize((int(awning_cleaner_image.width/4), int(awning_cleaner_image.height/4)))
        awning_cleaner_photo = ImageTk.PhotoImage(resized_awning_cleaner_image)

        item3 = tk.Label(shop_page)
        item3.image = awning_cleaner_photo
        item3.configure(image=awning_cleaner_photo)
        item3.grid(row=8, column=2, padx=20, pady=20)

        conn.commit()
        c.close()
            

        #Contact Us Function
        def contact_us():
            #Creating Contact Us Web Page
            contact_page = tk.Toplevel(window)
            contact_page.title("Contact Us Page")
            contact_page.geometry("900x550")
            contact_page.config(bg='#06CB30')
            
            #Company Title
            tk.Label(contact_page, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#06CB30', fg='white').grid(row=0, column=0)
            
            #Message on Contact Us Page
            tk.Label(contact_page, text="We value our customers. This is why we would like to hear from you. Leave your details below and we will get back to you shortly.", bg='#06CB30', fg='white').grid(row=1, column=0)
            
            #Getting Wye Camping Logo
            conn = sqlite3.connect('image.db')
            c = conn.cursor()

            # Retrieving the image data from the database
            c.execute("SELECT image_data FROM images WHERE image_id = ?", (1,))
            image_data = c.fetchone()[0]

            # Convert the image data to a Tkinter-compatible format
            image = Image.open(BytesIO(image_data))
            photo = ImageTk.PhotoImage(image)

            #Putting the logo image into a label and displaying it on the website
            logo_con = tk.Label(contact_page)
            logo_con.image = photo
            logo_con.configure(image=photo)
            logo_con.grid(row=0, column=2)

            #Commiting changes and Closing Connection
            conn.commit()
            c.close()

            #Home Button Function
            def return_home():
                contact_page.destroy()
                shop_page.tkraise()
            
            #Home Button
            tk.Button(contact_page, text="Home", command=return_home).grid(row=1, column=1)
            
            #Email Entry Box
            tk.Label(contact_page, text="Email: ", bg='#06CB30', fg='white').grid(row=2, column=0, padx=20, pady=20)
            contact_email = tk.Entry(contact_page)
            contact_email.grid(row=3, column=0, padx=20, pady=20)
            
            #Message Entry Box
            tk.Label(contact_page, text="Message: ", bg='#06CB30', fg='white').grid(row=4, column=0, padx=20, pady=20)
            contact_message = tk.Entry(contact_page, font=("Arial", 14), width=30)
            contact_message.grid(row=5, column=0, padx=20, pady=20)
            contact_message.insert(tk.END, "\n")

            #Generating Contact Request ID
            def generate_contact_id():
                contact_id = random.randint(0, 99)
                return contact_id

            #Submit Function
            def contact_submit():
                # Connect to the Customer Details database
                conn = sqlite3.connect('contact.db')

                # Create a table to store the user's information
                cursor = conn.cursor()
                
                #Putting the ID as a variable
                contact_id = generate_contact_id()
                email = contact_email.get()
                message = contact_message.get()

                # Insert a test user into the table
                cursor.execute('''INSERT INTO info VALUES (?, ?, ?)''', (contact_id, email, message))

                #Delete the data the user typed into the entries
                contact_email.delete(0, tk.END)
                contact_message.delete(0, tk.END)
                
                # Commit the changes
                conn.commit()
                
                #Closing Connection
                conn.close()
            
            
            #Submit Button
            tk.Button(contact_page, text="Submit.", command=contact_submit).grid(row=3, column=1)
    

        #Contact Us Button
        tk.Button(shop_page, text="Contact Us", command=contact_us).grid(row=3, column=0)
        
        #About Us Function
        def about_us():
            #Creating About Us Web Page
            about_page = tk.Toplevel(window)
            about_page.title("About Us Page")
            about_page.geometry("1500x550")
            about_page.config(bg='#06CB30')
            
            #Company Title
            tk.Label(about_page, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#06CB30', fg='white').grid(row=0, column=0)

            #Getting Wye Camping Logo
            conn = sqlite3.connect('image.db')
            c = conn.cursor()

            # Retrieving the image data from the database
            c.execute("SELECT image_data FROM images WHERE image_id = ?", (1,))
            image_data = c.fetchone()[0]

            # Convert the image data to a Tkinter-compatible format
            image = Image.open(BytesIO(image_data))
            photo = ImageTk.PhotoImage(image)

            #Putting the logo image into a label and displaying it on the website
            logo_abt = tk.Label(about_page)
            logo_abt.image = photo
            logo_abt.configure(image=photo)
            logo_abt.grid(row=0, column=2)

            #Commiting changes and Closing Connection
            conn.commit()
            c.close()
        
            #Message on About Us Page
            tk.Label(about_page, text="""We started our business in 2021, and from day one knew that by offering the best in all categories,
            we could make a big difference to our customers. In addition, our prices are competitive, and our service is simply superb.
            At Wye Camping And Leisure, our passion for excellence drove us from the beginning and continues to drive us today.
            To find out more, take a look at our website or get in touch with us!""", font=("Arial", 10), bg='#06CB30', fg='white').grid(row=2, column=0)
            
            #Message on About Us Page
            tk.Label(about_page, text="""It’s important to look after yourself when you're camping, and one sure-fire way of doing that is by eating well.
            We stock a diverse collection of water tap cartridges, eyelets, rain cowls, awning spreaders, and pole end.
            Whether you are a solo camper or are heading out in a group, we offer a wide range of quality products to best serve your camping needs.
            Get ready for your next camping trip!""", font=("Arial", 10), bg='#06CB30', fg='white').grid(row=3, column=0)
            
            #Message on About Us Page
            tk.Label(about_page, text="""Whether you're looking to head out on the wilderness adventure of a lifetime or you simply need new accessories and handles for your caravan?
            Then you owe it to yourself to see Wye Camping and Leisure, our online store. We supply our customers with top-of-the-line camping and caravan accessories gear to see them through when they head out into nature.
            Check our variety of adhesives, bag covers, towing items, catches, gas electricals, water sanitation, and awning and tent accessories.
            Give us a message on the form below and we’ll happily help you with any of your camping needs.""", font=("Arial", 10), bg='#06CB30', fg='white').grid(row=4, column=0)
            
            #Home Button Function
            def return_home():
                about_page.destroy()
                shop_page.tkraise()

            #Home Button
            tk.Button(about_page, text="Home", command=return_home).grid(row=1, column=1)
            
        #About Us Button
        tk.Button(shop_page, text="About Us", command=about_us).grid(row=3, column=2)

        #FAQ Page Function
        def faq():
            #Creating the FAQ Page
            faq_page = tk.Toplevel(window)
            faq_page.title("FAQ Page")
            faq_page.geometry("1500x550")
            faq_page.config(bg='#06CB30')

            #Company Title
            tk.Label(faq_page, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#06CB30', fg='white').grid(row=0, column=0, padx=20, pady=20)

            #FAQ Title
            tk.Label(faq_page, text="Frequently Asked Questions (FAQ) Page", font=("Arial", 16, "bold underline"), bg='#06CB30', fg='white').grid(row=1, column=0, padx=20, pady=20)

            #Getting Wye Camping Logo
            conn = sqlite3.connect('image.db')
            c = conn.cursor()

            # Retrieving the image data from the database
            c.execute("SELECT image_data FROM images WHERE image_id = ?", (1,))
            image_data = c.fetchone()[0]

            # Convert the image data to a Tkinter-compatible format
            image = Image.open(BytesIO(image_data))
            photo = ImageTk.PhotoImage(image)

            #Putting the logo image into a label and displaying it on the website
            logo_faq = tk.Label(faq_page)
            logo_faq.image = photo
            logo_faq.configure(image=photo)
            logo_faq.grid(row=0, column=3)

            #Message on FAQ Page
            tk.Label(faq_page, text="Welcome to our FAQ page! Here are some frequently asked questions and their corresponding answers:", font=("Arial", 12, "bold"), bg='#06CB30', fg='white').grid(row=2, column=0)

            #Message on FAQ Page
            tk.Label(faq_page, text="""
            Q: What is your return policy?
            A: We accept returns within 30 days of purchase, as long as the item is in its original packaging and condition. Please contact our customer service team to initiate a return.

            Q: How can I track my order?
            A: You will receive an email with tracking information once your order has shipped. You can also log in to your account on our website to view your order history and tracking information.

            Q: What payment methods do you accept?
            A: We accept all major credit cards, PayPal, and Apple Pay.

            Q: How long will it take for my order to arrive?
            A: Standard shipping typically takes 5-7 business days, but delivery times may vary depending on your location and shipping method selected at checkout.

            Q: Can I cancel my order?
            A: If your order has not yet shipped, you can contact our customer service team to request a cancellation. Once an order has shipped, it cannot be cancelled.""", font=("Arial", 10), bg='#06CB30', fg='white').grid(row=3, column=0)

            #Commiting changes and Closing Connection
            conn.commit()
            c.close()

        #FAQ Button
        tk.Button(shop_page, text="FAQ", command=faq).grid(row=4, column=0)
        
        #View Basket Button Function
        def view_basket():
                basket_window = tk.Toplevel(shop_page)
                basket_window.title("Basket")
                basket_window.geometry("1500x850")
                basket_window.config(bg='#06CB30')

                #Company Title
                tk.Label(basket_window, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#06CB30', fg='white').grid(row=0, column=2, padx=20, pady=20)

                #Basket Title
                tk.Label(basket_window, text="Customer Basket", font=("Arial", 16, "bold underline"), bg='#06CB30', fg='white').grid(row=1, column=2, padx=20, pady=20)

                #Message
                tk.Label(basket_window, text="These are the items in your basket:", font=("Arial", 16, "bold underline"), bg='#06CB30', fg='white').grid(row=2, column=2, padx=20, pady=20)

                # Create a frame to hold the basket items
                frame = tk.Frame(basket_window)
                frame.grid(row=3, column=0, columnspan=4)

                list_box = tk.Listbox(frame, width=80)

                # Insert headers as the first item in the listbox
                list_box.insert(tk.END, f"{'Product: ':<30} {'Quantity: ':<10} {'Price: (£)':<10}")

                #Populating the listbox with the items from the basket
                for i, basket_item in enumerate(basket):
                    list_box.insert(i+1, f"{basket_item[0]} {basket_item[1]} {basket_item[2]}")
                list_box.grid(row=0, column=0, columnspan= 4)
                
                # Add a button to close the basket window
                tk.Button(basket_window, text="Close", command=basket_window.destroy).grid(row=1, column=0, padx=10, pady=10)

                #CardNumber Entry Box
                tk.Label(basket_window, text="Please enter the long number on your card: ", bg='#06CB30', fg='white').grid(row=3, column=4, padx=20, pady=20)
                global card_name
                card_num = tk.Entry(basket_window, font=("Arial", 14), width=30)
                card_num.grid(row=4, column=4, padx=20, pady=20)
                card_num.insert(tk.END, "\n")

                #ExpiryNumber Entry Box
                tk.Label(basket_window, text="Please enter the expiry number on your card: ", bg='#06CB30', fg='white').grid(row=5, column=4, padx=20, pady=20)
                global expiry_num
                expiry_num = tk.Entry(basket_window, font=("Arial", 14), width=30)
                expiry_num.grid(row=6, column=4, padx=20, pady=20)
                expiry_num.insert(tk.END, "\n")

                #CVVNumber Entry Box
                tk.Label(basket_window, text="Please enter the CVV number on the back of your card: ", bg='#06CB30', fg='white').grid(row=7, column=4, padx=20, pady=20)
                global CVV_num
                CVV_num = tk.Entry(basket_window, font=("Arial", 14), width=30)
                CVV_num.grid(row=8, column=4, padx=20, pady=20)
                CVV_num.insert(tk.END, "\n")

                #Name Entry Box
                tk.Label(basket_window, text="Please enter the full name on your card: ", bg='#06CB30', fg='white').grid(row=9, column=4, padx=20, pady=20)
                global card_name
                card_name = tk.Entry(basket_window, font=("Arial", 14), width=30)
                card_name.grid(row=10, column=4, padx=20, pady=20)
                card_name.insert(tk.END, "\n")

                #Place Order Function
                def place_order():

                    global basket

                    find_product_id = ""
                    order_quantity = 0

                    #Connect to payments database
                    with sqlite3.connect('payment.db') as conn1:
                        c1 = conn1.cursor()

                        #Getting Payment Details
                        new_payment_id = random.randint(1000, 9999)
                        new_order_id = random.randint(1000, 9999)

                        def calculate_total_price(basket):
                            total = sum(item[1] * item[2] for item in basket)
                            return total

                        order_total_price = calculate_total_price(basket)
                        find_user_id = username_entry.get()
                        insert_card_name = card_name.get()
                        insert_CVV_num = CVV_num.get()
                        insert_expiry_num = expiry_num.get()
                        insert_card_num = card_num.get()

                        #Inserting variables into Payment database
                        c1.execute("INSERT INTO payments (payment_id, order_id, user_id, card_full_num, card_expiry, CVV, name_on_card, total_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (new_payment_id, new_order_id, find_user_id, insert_card_num, insert_expiry_num, insert_CVV_num, insert_card_name, order_total_price))

                        # Commit the changes and close the connection
                        conn1.commit()
                        c1.close()


                    #Connecting to Orders Database
                    with sqlite3.connect('shipping.db') as conn2:
                        c2 = conn2.cursor()

                        #Get Current date
                        def get_current_date():
                            now = datetime.datetime.now()
                            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
                            return formatted_date

                        # keep track of the selected item
                        selected_item = basket[0]

                        # find the total quantity for each product
                        product_quantities = {}
                        for item in basket:
                            product_id = item[0]
                            quantity = item[1]
                            if product_id in product_quantities:
                                product_quantities[product_id] += quantity
                            else:
                                product_quantities[product_id] = quantity

                        for item in basket:
                            #Getting Order Details
                            purch_date = get_current_date()

                            # convert purchase_date to a datetime object
                            format_string = '%Y-%m-%d %H:%M:%S'
                            purch_date = datetime.datetime.strptime(purch_date, format_string)

                            # add 4 days to purchase_date
                            deliv_date = purch_date + datetime.timedelta(days=4)

                            #if selected_item:
                            if selected_item == "Super Glue Twin Pack":
                                selected_item = find_product_id
                            elif selected_item == "Bungee Ball Cord Loop":
                                selected_item = find_product_id
                            elif selected_item == "Cleaning Brush Awning Rail":
                                selected_item = find_product_id

                            find_product_id = item[0]
                            order_quantity = product_quantities.get(find_product_id, 0)

                            # check if the record already exists
                            c2.execute("SELECT * FROM orders WHERE order_id=?", (new_order_id,))
                            result = c2.fetchone()

                            if result:
                                # update the existing record
                                c2.execute("UPDATE orders SET user_id=?, product_id=?, payment_id=?, total_price=?, delivery_date=?, purchase_date=?, quantity=? WHERE order_id=?", (find_user_id, find_product_id, new_payment_id, order_total_price, deliv_date, purch_date, order_quantity, new_order_id))
                            else:
                                # insert a new record
                                c2.execute("INSERT INTO orders (order_id, user_id, product_id, payment_id, total_price, delivery_date, purchase_date, quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (new_order_id, find_user_id, find_product_id, new_payment_id, order_total_price, deliv_date, purch_date, order_quantity))

                        # Commit the changes and close the connection
                        conn2.commit()
                        c2.close()

                # Place Order Button
                tk.Button(basket_window, text="Place Order", command=place_order).grid(row=4, column=1, padx=10, pady=10)

        #View Basket Button
        tk.Button(shop_page, text="View Basket", command=view_basket).grid(row=2, column=0)
        
        #Log Out Function
        def shop_logout():
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                shop_page.destroy()
                window.tkraise()
        
        #Log Out Button
        tk.Button(shop_page, text="Log out", command=shop_logout).grid(row=2, column=2)
    
    #Creating Application for Employees
    elif acc_type == "Employee":
        
        #Creating Employee's Page
        employee_page = tk.Toplevel(window)
        employee_page.title("Employee Work Application")
        employee_page.geometry("1400x650")    
        employee_page.config(bg='#239569')

        #Company Title
        tk.Label(employee_page, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#239569', fg='white').grid(row=0, column=2, padx=20, pady=20)

        #Employee Workstation Title
        tk.Label(employee_page, text="Employee Work Application", font=("Arial", 16, "bold underline"), bg='#239569', fg='white').grid(row=1, column=2, padx=20, pady=20)

        #Getting Wye Camping Logo
        conn = sqlite3.connect('image.db')
        c = conn.cursor()

        # Retrieving the image data from the database
        c.execute("SELECT image_data FROM images WHERE image_id = ?", (1,))
        image_data = c.fetchone()[0]

        # Convert the image data to a Tkinter-compatible format
        image = Image.open(BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)

        #Putting the logo image into a label and displaying it on the website
        logo_emp = tk.Label(employee_page)
        logo_emp.image = photo
        logo_emp.configure(image=photo)
        logo_emp.grid(row=0, column=3)

        #Commiting changes and Closing Connection
        conn.commit()
        c.close()
        
        #Text Prompt
        tk.Label(employee_page, text="What task would you like to perform?", font=("Arial", 14), bg='#239569', fg='white').grid(row=2, column=2)
        
        #Manage Product Information Function
        def manage_products():
            #Creating the window
            managing_products = tk.Tk()
            managing_products.title("Managing Products Workstation")
            managing_products.geometry("1000x650")
            managing_products.config(bg='#239569') 

            # Connect to the database
            conn = sqlite3.connect('stockroom.db')
            c = conn.cursor()
            
            #Company Title
            tk.Label(managing_products, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#239569', fg='white').pack()

            #Contact Customers Title
            tk.Label(managing_products, text="Managing Product Information Page", font=("Arial", 16), bg='#239569', fg='white').pack()

            #Product Name Entry Box
            tk.Label(managing_products, text='Product Name:', bg='#239569', fg='white').pack()
            product_entry_widget = tk.Entry(managing_products)
            product_entry_widget.pack()

            #Quantity Entry Box
            tk.Label(managing_products, text='Quantity:', bg='#239569', fg='white').pack()
            quantity_entry = tk.Entry(managing_products)
            quantity_entry.pack()

            #Price Entry Box
            tk.Label(managing_products, text='Price:', bg='#239569', fg='white').pack()
            price_entry = tk.Entry(managing_products)
            price_entry.pack()

            # Generate product id
            def generate_product_id():
                product_id = random.randint(0, 99)
                return product_id

            #Creates a random id number for a new order 
            def find_product_id(product_entry):
                # Connect to the database
                conn = sqlite3.connect('stockroom.db')
                c = conn.cursor()

                # Find the product's id based on its name
                prod_name = product_entry_widget.get()
                c.execute("SELECT product_id FROM products WHERE product_name=?", (prod_name,))
                result = c.fetchone()

                product_id = result[0] if result is not None else generate_product_id()

                return product_id

                # Close the database connection
                conn.commit()
                c.close()

            # Function to add a new item to the stock
            def add_item(product_entry_widget, quantity_entry, price_entry):
                #Retrive product id
                product_id = find_product_id(product_entry_widget)
                c.execute("INSERT INTO products (product_id, product_name, quantity, price) VALUES (?, ?, ?, ?)", (product_id, product_entry_widget, quantity_entry, price_entry))
                conn.commit()

                # Clear entry fields
                product_entry_widget.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)
            
            #Add Product Button
            tk.Button(managing_products, text="Add Product", command=lambda: add_item(product_entry_widget.get(), quantity_entry.get(), price_entry.get())).pack()

            # Function to update the quantity of an item in the stock
            def update_quantity(product_id, quantity_entry):
                product_id = find_product_id(product_entry_widget)
                new_quantity = quantity_entry.get()
                c.execute("UPDATE products SET quantity=? WHERE product_id=?", (new_quantity, product_id))
                conn.commit()
            
            #Update Product Button
            tk.Button(managing_products, text="Update Product", command=lambda: update_quantity(product_entry_widget, quantity_entry)).pack()

            # Function to update the price of an item in the stock
            def update_price(product_id, price_entry):
                product_id = find_product_id(product_entry_widget)
                new_price = price_entry.get()
                c.execute("UPDATE products SET price=? WHERE product_id=?", (new_price, product_id))
                conn.commit()
            
            #Update Price Button
            tk.Button(managing_products, text="Update Price", command=lambda: update_price(product_entry_widget, price_entry)).pack()

            #Home Button Function
            def home():
                managing_products.destroy()
                employee_page.tkraise()
        
            #Home Button
            tk.Button(managing_products, text="Home", command=home).pack(pady=5)

        #Manage Product Information Button
        tk.Button(employee_page, text="Manage Product Information", command=manage_products).grid(row=3, column=0)
        
        #Manage Stockroom Information Function
        def display_stockroom():
             # Connect to the database
            conn = sqlite3.connect('stockroom.db')
            c = conn.cursor()

            #Creating the window
            stockroom_overview = tk.Tk()
            stockroom_overview.title("Stockroom Overview")
            stockroom_overview.geometry("1000x450")
            stockroom_overview.config(bg='#239569')

            #Company Title
            tk.Label(stockroom_overview, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#239569', fg='white').pack()

            # Creating a frame to hold the listbox
            frame = tk.Frame(stockroom_overview, bg='#239569')
            frame.pack()

            #Stockroom Overview Title
            tk.Label(frame, text="Stockroom Overview", font=("Arial", 16, "bold underline"), bg='#239569', fg='white').grid(row=1, column=2)

            #View Stockroom information Function
            def display_items():
                c.execute("SELECT * FROM products")
                rows = c.fetchall()
                for row in rows:
                    item_id = row[0]
                    item_name = row[1]
                    item_quantity = row[2]
                    item_price = row[3]
                    # Add the item information to the listbox
                    item_listbox.insert(tk.END, f"{item_id}: {item_name}, {item_quantity}, £{item_price:.2f}")
            
            # Create a listbox to display the items
            item_listbox = tk.Listbox(frame, width=80)
            item_listbox.grid(row=3, column=1, columnspan=4)

            # Display all items in the database
            display_items()

            #Home Button Function
            def home():
                stockroom_overview.destroy()
                employee_page.tkraise()
        
            #Home Button
            tk.Button(frame, text="Home", command=home).grid(row=2, column=2)

            c.commit()
            c.close()
            
        
        #View Stockroom Information Button
        tk.Button(employee_page, text="View Stockroom Information", command=display_stockroom).grid(row=3, column=1)
        
        #View Shop Web Page Function
        def view_shop():
            employee_page.destroy()
            shop_page.tkraise()
        
        #View Shop Web Page Button
        tk.Button(employee_page, text="View Shop", command=view_shop).grid(row=3, column=2)
        
        #Contact Customers Function
        def contact_customers():
            # Create window
            contact_customers = tk.Toplevel()
            contact_customers.title("Contact Customers")
            contact_customers.geometry("1000x650")
            contact_customers.config(bg='#239569')

            #Company Title
            tk.Label(contact_customers, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#239569', fg='white').pack()

            #Contact Customers Title
            tk.Label(contact_customers, text="Contact Customers Page", font=("Arial", 16, "bold underline"), bg='#239569', fg='white').pack()

            # Connect to database
            conn = sqlite3.connect('login.db')
            c = conn.cursor()

            #Username Entry Box for Create an Account Page
            tk.Label(contact_customers, text='Username:', bg='#239569', fg='white').pack()
            username_entry = tk.Entry(contact_customers)
            username_entry.pack()

            #Querying the database
            def find_email():
                username = username_entry.get()
                c.execute('''SELECT email FROM users WHERE username=?''', (username,))
                result = c.fetchone()

                if result is not None:
                    email = result[0]
                    tk.Label(contact_customers, text=f"This customers email is {email}.").pack()
                else:
                    tk.Label(contact_customers, text="This customer does not have an email with us.").pack()
            
            #Home Button Function
            def home():
                contact_customers.destroy()
                employee_page.tkraise()
        
            #Home Button
            tk.Button(contact_customers, text="Home", command=home).pack(pady=5)
            
            #Contact Customers Button
            tk.Button(contact_customers, text="Find User's Email", command=find_email).pack()

            c.commit()
            c.close()
        
        #Contact Customers Button
        tk.Button(employee_page, text="Contact a Customer", command=contact_customers).grid(row=3, column=3)
        
        #Manage Order's Function
        def manage_orders():
            # Create window
            window = tk.Toplevel()
            window.title("Manage Orders")
            window.geometry("1200x850")
            window.config(bg='#239569')

            #Company Title
            tk.Label(window, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#239569', fg='white').pack()

            #Managing Orders Page Title
            tk.Label(window, text="Managing Orders Page", font=("Arial", 16, "bold underline"), bg='#239569', fg='white').pack()
    
            # Connect to database
            conn = sqlite3.connect('shipping.db')
            c = conn.cursor()

            # Function to display orders in the window
            def display_orders():
                # Clear existing orders
                for widget in window.winfo_children():
                    if widget.winfo_class() == 'Frame':
                        widget.destroy()
                
                # Retrieve orders from database
                c.execute("SELECT * FROM orders")
                orders = c.fetchall()
        
                # Create labels for orders
                for i, order in enumerate(orders):
                    order_frame = tk.Frame(window)
                    order_frame.pack(pady=5)
            
                    order_id = tk.Label(order_frame, text=order[0])
                    order_id.pack(side=tk.LEFT, padx=10)
            
                    customer_name = tk.Label(order_frame, text=order[1])
                    customer_name.pack(side=tk.LEFT, padx=10)
            
                    item_name = tk.Label(order_frame, text=order[2])
                    item_name.pack(side=tk.LEFT, padx=10)
            
                    delivery_date = tk.Label(order_frame, text=order[3])
                    delivery_date.pack(side=tk.LEFT, padx=10)

                    purchase_date = tk.Label(order_frame, text=order[4])
                    purchase_date.pack(side=tk.LEFT, padx=10)

                    quantity = tk.Label(order_frame, text=order[5])
                    quantity.pack(side=tk.LEFT, padx=10)

                    # Function to delete an order from the database
                    def delete_order():
                        # Delete order from database

                        order_id_int = order[0]
                        c.execute("DELETE FROM orders WHERE order_id=?", (order_id_int, ))
                        conn.commit()
                                
                        # Display updated orders
                        display_orders()
            
                    delete_button = tk.Button(order_frame, text="Delete", command=delete_order)
                    delete_button.pack(side=tk.LEFT, padx=10)
                
                conn.commit()
    
            def get_customer_id():
                username = customer_name_entry.get()

                # Connect to database
                conn = sqlite3.connect('login.db')
                c = conn.cursor()

                def find_user_id():
                    # Find user id based on username
                    c.execute("SELECT user_id FROM users WHERE username=?", (username,))
                    result = c.fetchone()

                if result is not None:
                    user_id = result[0]
                    print("User ID for username '{}' is {}.".format(username, user_id))
                else:
                    print("No user found with username '{}'.".format(username))

                # Close database connection
                conn.close()  
                return user_id

            def get_product_id():
                product = item_name_entry.get()

                # Connect to database
                conn = sqlite3.connect('stockroom.db')
                c = conn.cursor()

                def find_product_id():
                    # Find product id based on product_name
                    c.execute("SELECT product_id FROM products WHERE product=?", (product,))
                    result = c.fetchone()

                if result is not None:
                    product_id = result[0]
                    print("User ID for username '{}' is {}.".format(product, product_id))
                else:
                    print("No user found with username '{}'.".format(product))

                # Close database connection
                conn.close()  
                return product_id
            
            #Creates a random id number for a new order 
            def generate_order_id():
                order_id = random.randint(0, 99)
                return order_id

            # Function to add an order to the database
            def add_order():
                # Retrieve inputs from user
                order_id = generate_order_id()
                customer_id = get_customer_id() 
                product_id = get_product_id()
                delivery_date = delivery_date_entry.get()
                purchase_date = purchase_date_entry.get()
                quantity = quantity_entry.get()
        
                # Insert order into database
                c.execute("INSERT INTO orders (order_id, user_id, product_id, delivery_date, purchase_date, quantity) VALUES (?, ?, ?, ?, ?, ?)", (order_id, customer_id, product_id, delivery_date, purchase_date, quantity))
                conn.commit()
        
                # Clear input fields
                customer_name_entry.delete(0, tk.END)
                item_name_entry.delete(0, tk.END)
                delivery_date_entry.delete(0, tk.END)
                purchase_date_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
        
                # Display updated orders
                display_orders()

            # Create input fields for adding orders
            customer_name_label = tk.Label(window, text="Customer Username: ", bg='#239569', fg='white')
            customer_name_label.pack()
            customer_name_entry = tk.Entry(window)
            customer_name_entry.pack(pady=5)
                            
            item_name_label = tk.Label(window, text="Item Name: ", bg='#239569', fg='white')
            item_name_label.pack()
            item_name_entry = tk.Entry(window)
            item_name_entry.pack(pady=5)

            delivery_date_label = tk.Label(window, text="Delivery Date: ", bg='#239569', fg='white')
            delivery_date_label.pack()
            delivery_date_entry = tk.Entry(window)
            delivery_date_entry.pack(pady=5)

            purchase_date_label = tk.Label(window, text="Purchase Date: ", bg='#239569', fg='white')
            purchase_date_label.pack()
            purchase_date_entry = tk.Entry(window)
            purchase_date_entry.pack(pady=5)
                            
            quantity_label = tk.Label(window, text="Quantity: ", bg='#239569', fg='white')
            quantity_label.pack()
            quantity_entry = tk.Entry(window)
            quantity_entry.pack(pady=5)
                            
            add_button = tk.Button(window, text="Add Order", command=add_order)
            add_button.pack(pady=5)
    
            # Display existing orders
            display_orders()

            #Home Button Function
            def home():
                window.destroy()
                employee_page.tkraise()
        
            #Home Button
            tk.Button(window, text="Home", command=home).pack()
                                
            # Start main loop
            window.mainloop()
                                
            # Close database connection
            conn.close()
        
        #Manage Customer's Orders Button
        tk.Button(employee_page, text="Manage Customer Orders", command=manage_orders).grid(row=3, column=4)

        #View Contact Requests Function
        def contact_requests():

            #Creating Manager's Page
            contact_req_page = tk.Toplevel(window)
            contact_req_page.title("Contact Requests Overview")
            contact_req_page.geometry("1200x650")
            contact_req_page.config(bg='#239569')

            #Company Title
            tk.Label(contact_req_page, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#239569', fg='white').grid(row=0, column=0, padx=20, pady=20)

            #Contact Requests Overview Page Title
            tk.Label(contact_req_page, text="Contact Requests Overview Page", font=("Arial", 16, "bold underline"), bg='#239569', fg='white').grid(row=1, column=0, padx=20, pady=20)
        
            #Text Prompt
            tk.Label(contact_req_page, text="What would you like to inform us about?", font=("Arial", 14), bg='#239569', fg='white').grid(row=2, column=0)

            # Connect to the Customer Details database
            conn = sqlite3.connect('contact.db')

            # Create a table to store the user's information
            cursor = conn.cursor()
                
            # Retrieve orders from database
            cursor.execute("SELECT * FROM info")
            records = cursor.fetchall()
        
            scrollbar = tk.Scrollbar(contact_req_page)
            scrollbar.grid(row=3, column=2, sticky=tk.NS)
            text_widget = tk.Text(contact_req_page, yscrollcommand=scrollbar.set)
            text_widget.grid(row=3, column=1, sticky=tk.NSEW)
    
            # Insert the records into the text widget
            for record in records:
                text_widget.insert(tk.END, f'ID: {record[0]}\nEmail: {record[1]}\nMessage: {record[2]}\n\n')
    
            # Configure the scrollbar to work with the text widget
            scrollbar.config(command=text_widget.yview)

            #Home Button Function
            def home():
                contact_req_page.destroy()
                employee_page.tkraise()
        
            #Home Button
            tk.Button(contact_req_page, text="Home", command=home).pack(pady=5)

            # Commit the changes
            conn.commit()
                
            #Closing Connection
            conn.close()

        #Viw Contact Requests Button
        tk.Button(employee_page, text="View Contact Requests", command=contact_requests).grid(row=4, column=5)
        
        #Log Out Function
        def emp_logout():
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                employee_page.destroy()
                window.tkraise()
        
        #Log Out Button
        tk.Button(employee_page, text="Log out", command=emp_logout).grid(row=3, column=6)
        
    #Creating Managers Overview Application
    elif acc_type == "Manager":
        
        #Creating Manager's Page
        manager_page = tk.Toplevel(window)
        manager_page.title("Manager Overview Application")
        manager_page.geometry("1300x650")
        
        #Company Title
        tk.Label(manager_page, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline")).grid(row=0, column=2, padx=20, pady=20)

        #Manager Application Title
        tk.Label(manager_page, text="Manager Overview Application", font=("Arial", 16, "bold underline")).grid(row=1, column=2, padx=20, pady=20)
        
        #Text Prompt
        tk.Label(manager_page, text="What task would you like to perform?", font=("Arial", 14)).grid(row=2, column=2)
        
        #Manage Product Information Function
        def manage_products():
            # Connect to the database
            conn = sqlite3.connect('stockroom.db')
            c = conn.cursor()

            #Creating the window
            managing_products = tk.Tk()
            managing_products.title("Managing Products Workstation")
            managing_products.geometry("1000x650")
            
            #Company Title
            tk.Label(managing_products, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline")).pack()

            #Contact Customers Title
            tk.Label(managing_products, text="Managing Product Information Page", font=("Arial", 16)).pack()

            #Product Name Entry Box
            tk.Label(managing_products, text='Product Name:').pack()
            product_entry = tk.Entry(managing_products)
            product_entry.pack()

            #Quantity Entry Box
            tk.Label(managing_products, text='Quantity:').pack()
            quantity_entry = tk.Entry(managing_products)
            quantity_entry.pack()

            #Price Entry Box
            tk.Label(managing_products, text='Price:').pack()
            price_entry = tk.Entry(managing_products)
            price_entry.pack()

            # Generate product id
            def generate_product_id():
                product_id = random.randint(0, 99)
                return product_id

            #Creates a random id number for a new order 
            def find_product_id(product_entry):
                # Connect to the database
                conn = sqlite3.connect('stockroom.db')
                c = conn.cursor()

                # Find the product's id based on its name
                prod_name = product_entry.get()
                c.execute("SELECT product_id FROM products WHERE product_name=?", (prod_name,))
                result = c.fetchone()

                product_id = result[0] if result is not None else generate_product_id()

                return product_id

                # Close the database connection
                conn.close()
                c.close()

            # Function to add a new item to the stock
            def add_item(product_entry, quantity_entry, price_entry):
                #Retrive product id
                product_id = find_product_id(product_entry)
                c.execute("INSERT INTO products (product_id, product_name, quantity, price) VALUES (?, ?, ?, ?)", (product_id, product_entry, quantity_entry, price_entry))
                conn.commit()

                # Clear entry fields
                product_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
                price_entry.delete(0, tk.END)
            
            #Add Product Button
            tk.Button(managing_products, text="Add Product", command=lambda: add_item(product_entry.get(), quantity_entry.get(), price_entry.get())).pack()

            # Function to update the quantity of an item in the stock
            def update_quantity(product_id, quantity_entry):
                product_id = find_product_id(product_entry)
                new_quantity = quantity_entry.get()
                c.execute("UPDATE products SET quantity=? WHERE product_id=?", (new_quantity, product_id))
                conn.commit()
            
            #Update Product Button
            tk.Button(managing_products, text="Update Product", command=lambda: update_quantity(product_entry, quantity_entry)).pack()

            # Function to update the price of an item in the stock
            def update_price(product_id, price_entry):
                product_id = find_product_id(product_entry)
                new_price = price_entry.get()
                c.execute("UPDATE products SET price=? WHERE product_id=?", (new_price, product_id))
                conn.commit()
            
            #Update Price Button
            tk.Button(managing_products, text="Update Price", command=lambda: update_price(product_entry, price_entry)).pack()
        
        #Manage Product Information Button
        tk.Button(manager_page, text="Manage Product Information", command=manage_products).grid(row=3, column=0)
        
        #Manage Stockroom Information Function
        def display_stockroom():
             # Connect to the database
            conn = sqlite3.connect('stockroom.db')
            c = conn.cursor()

            #Creating the window
            stockroom_overview = tk.Tk()
            stockroom_overview.title("Stockroom Overview")
            stockroom_overview.geometry("1000x650")

            #Company Title
            tk.Label(stockroom_overview, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline")).grid(row=0, column=0)

            #Stockroom Overview Title
            tk.Label(stockroom_overview, text="Stockroom Overview", font=("Arial", 16, "bold underline")).grid(row=1, column=0)

            frame = tk.Frame(stockroom_overview, width=300, height=200, bg="white")
            frame.grid(row=3, column=0, columnspan=3)

            def display_items():
                c.execute("SELECT * FROM products")
                rows = c.fetchall()
                for row in rows:
                    item_id = row[0]
                    item_name = row[1]
                    item_quantity = row[2]
                    item_price = row[3]
                    # Add the item information to the listbox
                    item_listbox.insert(tk.END, f"{item_id}: {item_name}, {item_quantity}, £{item_price:.2f}")
            
            # Create a listbox to display the items
            item_listbox = tk.Listbox(frame, width=80)
            item_listbox.grid(row=0, column=0, columnspan=3)

            # Display all items in the database
            display_items()

            conn.commit()
            c.close()
        
        #Manage Stockroom Information
        tk.Button(manager_page, text="Manage Stockroom Information", command=display_stockroom).grid(row=3, column=1)
        
        #Contact Customers Function
        def contact_customers():
            # Create window
            contact_customers = tk.Toplevel()
            contact_customers.title("Contact Customers")

            #Company Title
            tk.Label(contact_customers, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline")).pack()

            #Contact Customers Title
            tk.Label(contact_customers, text="Contact Customers Page", font=("Arial", 16, "bold underline")).pack()

            # Connect to database
            conn = sqlite3.connect('login.db')
            c = conn.cursor()

            #Username Entry Box for Create an Account Page
            tk.Label(contact_customers, text='Username:').pack()
            username_entry = tk.Entry(contact_customers)
            username_entry.pack()

            #Querying the database
            def find_email():
                username = username_entry.get()
                c.execute('''SELECT email FROM users WHERE username=?''', (username,))
                result = c.fetchone()

                if result is not None:
                    email = result[0]
                    tk.Label(contact_customers, text=f"This customers email is {email}.").pack()
                else:
                    tk.Label(contact_customers, text="This customer does not have an email with us.").pack()
            
            #Home Button Function
            def home():
                contact_customers.destroy()
                employee_page.tkraise()
        
            #Home Button
            tk.Button(contact_customers, text="Home", command=home).pack(pady=5)
            
            #Contact Customers Button
            tk.Button(contact_customers, text="Find User's Email", command=find_email).pack()

            c.commit()
            c.close()
        
        #Contact Customers Button
        tk.Button(manager_page, text="Contact a Customer", command=contact_customers).grid(row=3, column=3)

        #View Contact Requests Function
        def contact_requests():

            #Creating Manager's Page
            contact_req_page = tk.Toplevel(window)
            contact_req_page.title("Contact Requests Overview")
            contact_req_page.geometry("1200x650")

            #Company Title
            tk.Label(contact_req_page, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline")).grid(row=0, column=0, padx=20, pady=20)

            #Contact Requests Overview Page Title
            tk.Label(contact_req_page, text="Contact Requests Overview Page", font=("Arial", 16, "bold underline")).grid(row=1, column=0, padx=20, pady=20)
        
            #Text Prompt
            tk.Label(contact_req_page, text="What task would you like to perform?", font=("Arial", 14)).grid(row=2, column=0)

            # Connect to the Customer Details database
            conn = sqlite3.connect('contact.db')

            # Create a table to store the user's information
            cursor = conn.cursor()
                
            # Retrieve orders from database
            cursor.execute("SELECT * FROM info")
            records = cursor.fetchall()
        
            scrollbar = tk.Scrollbar(contact_req_page)
            scrollbar.grid(row=3, column=2, sticky=tk.NS)
            text_widget = tk.Text(contact_req_page, yscrollcommand=scrollbar.set)
            text_widget.grid(row=3, column=1, sticky=tk.NSEW)
    
            # Insert the records into the text widget
            for record in records:
                text_widget.insert(tk.END, f'ID: {record[0]}\nEmail: {record[1]}\nMessage: {record[2]}\n\n')
    
            # Configure the scrollbar to work with the text widget
            scrollbar.config(command=text_widget.yview)

            # Commit the changes
            conn.commit()
                
            #Closing Connection
            conn.close()

        #View Contact Requests Button
        tk.Button(manager_page, text="View Contact Requests", command=contact_requests).grid(row=4, column=5)
        
        #Manage Customer's Orders Function
        def manage_orders():
            # Create window
            window = tk.Toplevel()
            window.title("Manage Orders")
            window.geometry("1200x850")

            #Company Title
            tk.Label(window, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline")).pack()

            #Managing Orders Page Title
            tk.Label(window, text="Managing Orders Page", font=("Arial", 16, "bold underline")).pack()
    
            # Connect to database
            conn = sqlite3.connect('shipping.db')
            c = conn.cursor()

            # Function to display orders in the window
            def display_orders():
                # Clear existing orders
                for widget in window.winfo_children():
                    if widget.winfo_class() == 'Frame':
                        widget.destroy()
                
                # Retrieve orders from database
                c.execute("SELECT * FROM orders")
                orders = c.fetchall()
        
                # Create labels for orders
                for i, order in enumerate(orders):
                    order_frame = tk.Frame(window)
                    order_frame.pack(pady=5)
            
                    order_id = tk.Label(order_frame, text=order[0])
                    order_id.pack(side=tk.LEFT, padx=10)
            
                    customer_name = tk.Label(order_frame, text=order[1])
                    customer_name.pack(side=tk.LEFT, padx=10)
            
                    item_name = tk.Label(order_frame, text=order[2])
                    item_name.pack(side=tk.LEFT, padx=10)
            
                    delivery_date = tk.Label(order_frame, text=order[3])
                    delivery_date.pack(side=tk.LEFT, padx=10)

                    purchase_date = tk.Label(order_frame, text=order[4])
                    purchase_date.pack(side=tk.LEFT, padx=10)

                    quantity = tk.Label(order_frame, text=order[5])
                    quantity.pack(side=tk.LEFT, padx=10)

                    # Function to delete an order from the database
                    def delete_order():
                        # Delete order from database
                        c.execute("DELETE FROM orders WHERE order_id=?", (order_id,))
                        conn.commit()
                                
                        # Display updated orders
                        display_orders()
            
                    delete_button = tk.Button(order_frame, text="Delete", command=delete_order)
                    delete_button.pack(side=tk.LEFT, padx=10)
                
                c.commit()
                c.close()
    
            def get_customer_id():
                username = customer_name_entry.get()

                # Connect to database
                conn = sqlite3.connect('login.db')
                c = conn.cursor()

                def find_user_id():
                    # Find user id based on username
                    c.execute("SELECT user_id FROM users WHERE username=?", (username,))
                    result = c.fetchone()

                if result is not None:
                    user_id = result[0]
                    print("User ID for username '{}' is {}.".format(username, user_id))
                else:
                    print("No user found with username '{}'.".format(username))

                # Close database connection
                conn.close()  
                return user_id

            def get_product_id():
                product = item_name_entry.get()

                # Connect to database
                conn = sqlite3.connect('stockroom.db')
                c = conn.cursor()

                def find_product_id():
                    # Find product id based on product_name
                    c.execute("SELECT product_id FROM products WHERE product=?", (product,))
                    result = c.fetchone()

                if result is not None:
                    product_id = result[0]
                    print("User ID for username '{}' is {}.".format(product, product_id))
                else:
                    print("No user found with username '{}'.".format(product))

                # Close database connection
                conn.close()  
                return product_id
            
            #Creates a random id number for a new order 
            def generate_order_id():
                order_id = random.randint(0, 99)
                return order_id

            # Function to add an order to the database
            def add_order():
                # Retrieve inputs from user
                order_id = generate_order_id()
                customer_id = get_customer_id() 
                product_id = get_product_id()
                delivery_date = delivery_date_entry.get()
                purchase_date = purchase_date_entry.get()
                quantity = quantity_entry.get()
        
                # Insert order into database
                c.execute("INSERT INTO orders (order_id, user_id, product_id, delivery_date, purchase_date, quantity) VALUES (?, ?, ?, ?, ?, ?)", (order_id, customer_id, product_id, delivery_date, purchase_date, quantity))
                conn.commit()
        
                # Clear input fields
                customer_name_entry.delete(0, tk.END)
                item_name_entry.delete(0, tk.END)
                delivery_date_entry.delete(0, tk.END)
                purchase_date_entry.delete(0, tk.END)
                quantity_entry.delete(0, tk.END)
        
                # Display updated orders
                display_orders()

            # Create input fields for adding orders
            customer_name_label = tk.Label(window, text="Customer Username: ")
            customer_name_label.pack()
            customer_name_entry = tk.Entry(window)
            customer_name_entry.pack(pady=5)
                            
            item_name_label = tk.Label(window, text="Item Name: ")
            item_name_label.pack()
            item_name_entry = tk.Entry(window)
            item_name_entry.pack(pady=5)

            delivery_date_label = tk.Label(window, text="Delivery Date: ")
            delivery_date_label.pack()
            delivery_date_entry = tk.Entry(window)
            delivery_date_entry.pack(pady=5)

            purchase_date_label = tk.Label(window, text="Purchase Date: ")
            purchase_date_label.pack()
            purchase_date_entry = tk.Entry(window)
            purchase_date_entry.pack(pady=5)
                            
            quantity_label = tk.Label(window, text="Quantity: ")
            quantity_label.pack()
            quantity_entry = tk.Entry(window)
            quantity_entry.pack(pady=5)
                            
            add_button = tk.Button(window, text="Add Order", command=add_order)
            add_button.pack(pady=5)
    
            # Display existing orders
            display_orders()

            #Home Button Function
            def home():
                window.destroy()
                employee_page.tkraise()
        
            #Home Button
            tk.Button(window, text="Home", command=home).pack(pady=5)
                                
            # Start main loop
            window.mainloop()
                                
            # Close database connection
            conn.close()
        
        
        #Manage Customer's Orders Button
        tk.Button(manager_page, text="Manage Customer Orders", command=manage_orders).grid(row=3, column=4)
     
        #Home Button Function
        def man_home():
            manager_page.destroy()
            manager_page.tkraise()
        
        #Home Button
        tk.Button(manager_page, text="Home", command=man_home).grid(row=4, column=1)
        
        #Log Out Function
        def man_logout():
                username_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                manager_page.destroy()
                window.tkraise()
        
        #Log Out Button
        tk.Button(manager_page, text="Log out", command=man_logout).grid(row=4, column=2)
        
    else:
        tk.Label(window, text='Invalid username or password').grid(row=6, column=1)
    
    # Close the connection
    conn.close()

# Create a login button
tk.Button(window, text='Login', command=check_login).grid(row=8, column=0, pady=10)

# Create a function to create a new account
def create_account():
    # Open a new window for the create account form
    create_window = tk.Toplevel(window)
    create_window.title('Create Account')
    create_window.config(bg='#06CB30')

    #Company Title
    tk.Label(create_window, text="Wye Camping & Leisure", font=("Arial", 18, "bold underline"), bg='#06CB30', fg='white').grid(row=0, column=0, padx=20, pady=20)

    #Manager Application Title
    tk.Label(create_window, text="Create an Account Window", font=("Arial", 16, "bold underline"), bg='#06CB30', fg='white').grid(row=1, column=0)
    
    # Create the form to enter the new account details
    tk.Label(create_window, text='Please put your account details in below.', bg='#06CB30', fg='white').grid(row=2, column=0)
    
    #Username Entry Box for Create an Account Page
    tk.Label(create_window, text='Username:', bg='#06CB30', fg='white').grid(row=3, column=0)
    create_username_entry = tk.Entry(create_window)
    create_username_entry.grid(row=4, column=0, padx=20, pady=20)
    
    #Password Entry Box for Create an Account Page
    tk.Label(create_window, text='Password:', bg='#06CB30', fg='white').grid(row=5, column=0)
    create_password_entry = tk.Entry(create_window, show='*')
    create_password_entry.grid(row=6, column=0, padx=20, pady=20)

    #Email Entry for Create an Account Page
    tk.Label(create_window, text='Email:', bg='#06CB30', fg='white').grid(row=7, column=0)
    create_email_entry = tk.Entry(create_window)
    create_email_entry.grid(row=8, column=0, padx=20, pady=20)

    #Account Type Entry for Create an Account Page
    tk.Label(create_window, text='Account Type:', bg='#06CB30', fg='white').grid(row=9, column=0)
    account_type_var = tk.StringVar(create_window)
    account_type_menu = tk.OptionMenu(create_window, account_type_var, 'Customer', 'Employee', 'Manager')
    account_type_menu.grid(row=10, column=0, padx=20, pady=20)
    
    # Create a function to save the new account to the database
    def save_account():
        # Connect to the database
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
    
        def generate_id(length=10):
            """Generate a random ID string of the specified length"""
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
            return ''.join(random.choice(letters) for i in range(length))

        account_type = account_type_var.get()
        if account_type in ['Employee', 'Manager']:
            pass_key = simpledialog.askstring("Pass Key", f"Enter the pass key for {account_type} accounts")
            if not pass_key:
                messagebox.showerror("Error", "Pass key is required for this account type.")
                return
            elif account_type == 'Employee' and pass_key != 'type2passkey':
                messagebox.showerror("Error", "Incorrect pass key.")
                return
            elif account_type == 'Manager' and pass_key != 'type3passkey':
                messagebox.showerror("Error", "Incorrect pass key.")
                return
    
        # Insert the new account into the table
        cursor.execute('''INSERT INTO users VALUES (?, ?, ?, ?, ?)''', (generate_id(), create_username_entry.get(), create_password_entry.get(), account_type, create_email_entry.get()))
    
        #Clearing screen
        create_username_entry.delete(0, tk.END)
        create_password_entry.delete(0, tk.END)
        create_email_entry.delete(0, tk.END)
        create_window.destroy()

        # Commit the changes
        conn.commit()
    
        # Close the connection
        conn.close()
        
    # Create a save button
    tk.Button(create_window, text='Save', command=save_account).grid(row=11, column=0, pady=10)

# Create a an account button
tk.Button(window, text='Create an Account', command=create_account).grid(row=9, column=0, pady=10)

#Close Program Function
def close_program():
    window.destroy()

#Close Program Button
tk.Button(window, text='Close Program', command=close_program).grid(row=11, column=0, pady=10)

# Run the main loop
window.mainloop()