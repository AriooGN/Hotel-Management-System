import customtkinter as ctk
import threading
from tkinter import messagebox
from oracleDB import OracleDBConnect as oracle
from TableView import TableViewForm as tableview
from utils import *
import random as rd


# Function to check login credentials in a separate thread
def check_login_threaded():
    # Disabling UI elements
    username_entry.configure(state='disabled')
    password_entry.configure(state='disabled')
    login_button.configure(state='disabled')
    if(str(password_entry) == '04295930' or str(username_entry) == 'ppourman'):
        messagebox.showerror("Error", f"Login Failed: Incorrect Credentials")
        return
    try:
        username = username_entry.get()
        password = password_entry.get()
        
        global db
        db = oracle(username=str(username), password=str(password))
        if(db.is_connected):
            show_database_options()
            messagebox.showinfo("Login Successful", 'You have successfully logged in.')
        else:
            messagebox.showerror("Error", f"Login Failed: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        db.close()
        db = ''
    finally:
        # Re-enabling UI elements
        
        username_entry.configure(state='normal')
        password_entry.configure(state='normal')
        login_button.configure(state='normal')

def submit_passenger_id(customer_id, phone, email, form_window):
    # Utilizing validate_field for validation checks
    if not validate_field(customer_id, "Customer ID", "int"):
        return
    if not validate_field(phone, "Phone", "phone"):
        return
    if not validate_field(email, "Email", "email"):
        return
    
    sql_command = "INSERT INTO Passenger_ID (Customer_Id, Phone, Email) VALUES (:Cid, :phone, :email)"
    sql_params = {'Cid': customer_id, 'phone': phone, 'email': email}
    # Proceed with the database operation
    db.execute_SQL_commands(sql_commands=sql_command, command_params=[sql_params])
    # Close the form window
    form_window.destroy()

def submit_passenger_info(phone, email, first_name, middle_name, last_name, city, postal_code, street, province, form_window):
    if not validate_field(phone, "Phone", "phone"):
        return
    if not validate_field(email, "Email", "email"):
        return
    if not validate_field(first_name, "First Name", "string"):
        return
    if not validate_field(middle_name, "Middle Name", "string"):
        return
    if not validate_field(last_name, "Last Name", "string"):
        return
    if not validate_field(city, "City", "string"):
        return
    if not validate_field(postal_code, "Postal Code", "string"):
        return
    if not validate_field(street, "Street", "string"):
        return
    if not validate_field(province, "Province", "string"):
        return
    sql_command = """
        INSERT INTO Passenger_INFO 
        (Phone, Email, FirstN, MiddleN, LastN, City, PostalCode, Street, Province)
        VALUES (:phone, :email, :first_name, :middle_name, :last_name, :city, :postal_code, :street, :province)
        """
    sql_params = {
                    'phone': phone, 
                    'email': email, 
                    'first_name': first_name, 
                    'middle_name': middle_name, 
                    'last_name': last_name, 
                    'city': city, 
                    'postal_code': postal_code, 
                    'street': street, 
                    'province': province
    }

    # Insert data into the database
    try:
        db.execute_SQL_commands(sql_commands=sql_command,command_params=[sql_params])
        form_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def submit_personnel_id(nin, first_name, middle_name, last_name, form_window):
    if not validate_field(nin, "NIN", "int"):
        return
    if not validate_field(first_name, "First Name", "string"):
        return
    if middle_name and not validate_field(middle_name, "Middle Name", "string"):
        return
    if not validate_field(last_name, "Last Name", "string"):
        return
    sql_params = {
        'nin': nin, 
        'first_name': first_name, 
        'middle_name': middle_name if middle_name else None,  # Assuming middle name can be null
        'last_name': last_name if last_name else None  # Assuming last name can be null
    }

    sql_command = """
        INSERT INTO Personnel_ID (NIN, FirstN, MiddleN, LastN)
        VALUES (:nin, :first_name, :middle_name, :last_name)
        """
    # Insert data into the database
    try:
        # Assuming the db object has a method insert_personnel_id to insert the data
        # You'll need to create this method in your db class
        db.execute_SQL_commands(sql_commands=sql_command,command_params=[sql_params])
        form_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def submit_personnel_info(nin, salary, date_of_birth, street, home_number, city, province, postal_code, form_window):
    if not nin.isdigit():
        messagebox.showerror("Invalid Input", "NIN should be a number")
        return
    if not salary.isdigit():
        messagebox.showerror("Invalid Input", "Salary should be a number")
        return
    sql_command = """
        INSERT INTO Personnel_INFO (NIN, Salary, Date_of_Birth, Street, Home_Number, City, Province, PostalCode)
        VALUES (:nin, :salary, TO_DATE(:date_of_birth, 'YYYY-MM-DD')    , :street, :home_number, :city, :province, :postal_code)
    """
    sql_params =  {
        'nin': nin,
        'salary': salary,
        'date_of_birth': date_of_birth,
        'street': street,
        'home_number': home_number,
        'city': city,
        'province': province,
        'postal_code': postal_code
    }

    try:
        db.execute_SQL_commands(sql_commands=sql_command,command_params=[sql_params])
        form_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def submit_room_info(room_number, bedsize, room_type, price, form_window):
    # Validate each field
    if not validate_field(room_number, "Room Number", "int"):
        return
    if not validate_field(bedsize, "Size of Bed", "string"):
        return
    if not validate_field(room_type, "Room Type", "string"):
        return
    if price and not validate_field(price, "Price Per Night", "decimal"):
        return

    # Convert room number and price to the appropriate data types
    room_number = int(room_number)
    price = float(price) if price else None

    # Call the insert_room function with the validated data
    try:
        db.insert_room(room_number, bedsize, room_type, price)
        form_window.destroy()  # Close the form window after successful insertion
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def check_login(event=None):  # Accept an optional event parameter
    threading.Thread(target=check_login_threaded).start()

def toggle_password(checkbox_state):
    if checkbox_state.get() == 1:  # Checkbox is checked
        password_entry.configure(show="")
    else:  # Checkbox is not checked
        password_entry.configure(show="*")

def show_database_options():
    # Hide login elements
    username_label.grid_remove()
    username_entry.grid_remove()
    password_label.grid_remove()
    password_entry.grid_remove()
    show_password_checkbox.grid_remove()
    login_button.grid_remove()

    # Show database operation buttons
    for index, button in enumerate(main_menu_database_buttons):
        row_padding = (10, 5) if index % 2 == 0 else (5, 10)
        button.grid(row=index, column=0, pady=row_padding, padx=5)
    app.geometry("155x260")

def back_from_insert_queries():
        for button in queries_screen_buttons:
            button.grid_remove()
        show_database_options()

def queries_screen():
    app.geometry("155x250")
    for index, button in enumerate(main_menu_database_buttons):
        button.grid_remove()

    for index, button in enumerate(queries_screen_buttons):
        if(button == queries_screen_buttons[-1]):
            button.grid(row=index, column=0, pady=20, padx=5)
            break
        button.grid(row=index, column=0, pady=5, padx=5)

def insert_data_screen():
    app.geometry("155x325")
    for index, button in enumerate(main_menu_database_buttons):
        button.grid_remove()
    
    
    for index, button in enumerate(table_buttons_insert_data_screen):
        if(button == table_buttons_insert_data_screen[-1]):
            button.grid(row=index, column=0, pady=20, padx=5)
            break
        button.grid(row=index, column=0, pady=5, padx=5)
    
def back_from_insert_data_screen():
    for button in table_buttons_insert_data_screen:
        button.grid_remove()

        show_database_options()

def open_passenger_id_form():
    form_window = ctk.CTkToplevel()
    form_window.title("Enter Passenger ID Details")
    # Fields to be included in the form
    fields = ["Customer ID", "Phone (10 digits)", "Email (max 100 characters)"]
    # Create form fields
    entries = create_form(form_window=form_window, fields=fields)
    # Submit button with command
    submit_button = ctk.CTkButton(
        form_window, 
        text="Submit", 
        command=lambda: submit_passenger_id(
            entries["Customer ID"].get(),
            entries["Phone (10 digits)"].get(),
            entries["Email (max 100 characters)"].get(),
            form_window=form_window
        )
    )
    submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

def open_payment_form():
    form_window = ctk.CTkToplevel()
    form_window.title("Enter Payment Details")
    # Fields to be included in the form
    fields = ["PaymentID", "PaymentAmount", "TransactionType"]
    # Create form fields
    entries = create_form(form_window=form_window, fields=fields)
    # Submit button with command
    submit_button = ctk.CTkButton(
        form_window, 
        text="Submit", 
        command=lambda: submit_payment_form(
            entries["PaymentID"].get(),
            entries["PaymentAmount"].get(),
            entries["TransactionType"].get(),
            form_window=form_window
        )
    )
    submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)
    

def submit_payment_form(Payment_ID, Payment_Amount, Transaction_Type, form_window):

    # Utilizing validate_field for validation checks
    if not validate_field(Payment_ID, "Payment ID", "int"):
        return
    if not validate_field(Payment_Amount, "Payment Amount", "int"):
        return
    if not validate_field(Transaction_Type, "Transaction Type", "string"):
        return
    
    sql_command = """INSERT INTO Payment (Payment_Id, PaymentAmount, TransactionType) 
                     VALUES (:paymentId, :paymentAmount, :transactionType)"""
    sql_params = [{'paymentId': Payment_ID, 
                  'paymentAmount': Payment_Amount, 
                  'transactionType': Transaction_Type
                }]
    print(sql_command)
    # Proceed with the database operation
    db.execute_SQL_commands(sql_commands=sql_command, command_params=sql_params)
    
    # Close the form window
    form_window.destroy()

def open_passenger_info_form():
    form_window = ctk.CTkToplevel()
    form_window.title("Enter Passenger Info")
    fields = [
        "Phone (10 digits)", "Email (max 100 characters)", "First Name", 
        "Middle Name", "Last Name", "City", "Postal Code", "Street", "Province"
    ]
    entries = create_form(form_window, fields)

    submit_button = ctk.CTkButton(
        form_window, 
        text="Submit", 
        command=lambda: submit_passenger_info(
            *[entries[field].get() for field in fields], form_window=form_window
        )
    )
    submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

def open_personnel_id_form():
    form_window = ctk.CTkToplevel()
    form_window.title("Enter Personnel ID Details")
    fields = ["NIN", "First Name", "Middle Name", "Last Name"]
    entries = create_form(form_window, fields)

    submit_button = ctk.CTkButton(
        form_window, 
        text="Submit", 
        command=lambda: submit_personnel_id(
            *[entries[field].get() for field in fields], form_window=form_window
        )
    )
    submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

def open_personnel_info_form():
    form_window = ctk.CTkToplevel()
    form_window.title("Enter Personnel Info")
    fields = ["NIN", "Salary", "Date of Birth (YYYY-MM-DD)", "Street", "Home Number", "City", "Province", "Postal Code"]
    entries = create_form(form_window, fields)

    submit_button = ctk.CTkButton(
        form_window, 
        text="Submit",
        command=lambda: submit_personnel_info(
            *[entries[field].get() for field in fields], form_window=form_window
        )
    )
    submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

def open_room_form():
    form_window = ctk.CTkToplevel()
    form_window.title("Enter Room Info")
    
    # Define the fields and dropdown options
    fields = ["Room Number", "Size of Bed", "Room Type", "Price Per Night"]
    dropdowns = {
        "Room Type": ["Single", "Twin", "King"]
    }

    # Create form with fields and dropdowns
    entries = create_form(form_window, fields, dropdowns)

    # Submit button with a command to collect form data and process it
    submit_button = ctk.CTkButton(
        form_window, 
        text="Submit",
        command=lambda: submit_room_info(
            *[entries[field].get() for field in fields], form_window=form_window
        )
    )

    submit_button.grid(row=len(fields) + 1, column=0, columnspan=2, pady=10)

def open_reservation_form():
    form_window = ctk.CTkToplevel()
    form_window.title("Enter Reservation Info")
    
    # Define the fields and dropdown options
    reservation_fields = ["Reservation ID", "Check-In Date YYYY-MM-DD", "Check-Out Date YYYY-MM-DD"]
    # Create form with fields and dropdowns
    entries = create_form(form_window, reservation_fields)

    # Submit button with a command to collect form data and process it
    submit_button = ctk.CTkButton(
        form_window, 
        text="Submit",
        command=lambda: submit_reservation_info(
            *[entries[field].get() for field in reservation_fields], form_window=form_window
        )
    )

    submit_button.grid(row=len(reservation_fields) + 1, column=0, columnspan=2, pady=10)

def submit_reservation_info(reservation_id, checkin_date, checkout_date, form_window):

    sql_command = """INSERT INTO Reservation (Reservation_ID, CheckInDate, CheckOutDate) VALUES (:reservation_id, TO_DATE(':check_in_date', 'YYYY-MM-DD'), TO_DATE(':check_out_date', 'YYYY-MM-DD'))"""

    sql_params =  {
        'reservation_id': reservation_id,
        'check_in_date': checkin_date,
        'check_out_date': checkout_date
    }

    try:
        db.execute_SQL_commands(sql_commands=sql_command,command_params=sql_params)
        form_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def DropTablesUI():
    db.drop_tables()

def CreateTablesUI():
    db.create_tables()
    
def PopulateTablesUI():
    db.populate_tables()

def passanger_query():
    query = db.passenger_query()
    print(len(query))
    labels = ["ID", "Phone Number", "Email", "First Name", "Middle Name", "Last Name", "City", "Postal Code", "Street Name", "Province"]
    tbv = tableview(root=app,data=query)
    tbv.set_labels(labels=labels)
    tbv.display()

def personnel_query():
    query = db.personnel_query()
    labels = ["NIN", "First Name", "Middle Name", "Last Name", "Salary", "DOB", "Street", "Home Number", "City", "Province", "PostalCode"]
    tbv = tableview(root=app,data=query)
    tbv.set_labels(labels=labels)
    tbv.display()

def room_query():
    query = db.room_query()
    labels = ["RoomNumber", "NumberOfBeds", "PricePerNight", "RoomType"]
    tbv = tableview(root=app,data=query)
    tbv.set_labels(labels=labels)
    tbv.display()

def payment_query():
    query = db.payment_query()
    labels = ["Payment_ID", "PaymentAmount", "TransactionType"]
    tbv = tableview(root=app,data=query)
    tbv.set_labels(labels=labels)
    tbv.display()

def reservation_query():
    query = db.reservation_query()
    print(query)
    labels = ["Reservation_ID", "Check In", "Check Out"]
    tbv = tableview(root=app,data=query)
    tbv.set_labels(labels=labels)
    tbv.display()

def on_close():
    global db
    try:
        if db != None and isinstance(db,oracle): 
            db.close()
    except:
        print
        app.destroy()
    
    app.destroy()

# Creating the main window
global db
app = create_root("Database Operations", size=(280, 125), resizable=(False, False))
app.protocol("WM_DELETE_WINDOW", on_close)

# Create the username label and entry
username_label, username_entry = create_label_entry(app, "Username:", 0, pady=(10, 3), padx=10)

# Create the password label and entry
password_label, password_entry = create_label_entry(app, "Password:", 1, pady=(3, 10), padx=10)
password_entry.configure(show="*")

# Checkbox for showing/hiding password
checkbox_state = ctk.IntVar()
show_password_checkbox = ctk.CTkCheckBox(app, text="", variable=checkbox_state, command=lambda: toggle_password(checkbox_state), width=5, height=5)
show_password_checkbox.grid(row=1, column=2, pady=2, padx=0)

# Adding a login button
login_button = ctk.CTkButton(app, text="Login", command=check_login)
login_button.grid(row=2, column=1, pady=0, padx=5)

# Binds for log in screen (so enter works)
username_entry.bind("<Return>", check_login)
password_entry.bind("<Return>", check_login)

# Database operation buttons (hidden initially)
insert_data_button = ctk.CTkButton(app, text="Insert Data", command=insert_data_screen)
populate_tables_button = ctk.CTkButton(app, text="Populate Tables", command=PopulateTablesUI)
drop_tables_button = ctk.CTkButton(app, text="Drop Tables", command=DropTablesUI)
create_tables_button = ctk.CTkButton(app, text="Create Tables", command=CreateTablesUI)
query_tables_button = ctk.CTkButton(app, text="Queries", command=queries_screen)
exit_button = ctk.CTkButton(app, text="Exit", command=on_close, fg_color='red', hover_color='red4')

main_menu_database_buttons = [
    insert_data_button, populate_tables_button, drop_tables_button,
    create_tables_button, query_tables_button, exit_button
]
# Insert Data Screen

# Define buttons for each table
tables = {
    "Passenger_ID": open_passenger_id_form,
    "Passenger Info": open_passenger_info_form,
    "personnel_ID": open_personnel_id_form,
    "Personnel Info": open_personnel_info_form,
    "Rooms" : open_room_form,
    "Payment" : open_payment_form,
    "Reservation" : open_reservation_form
}

table_buttons_insert_data_screen = []

for button_name, button_function in tables.items():
    button = ctk.CTkButton(app, text=button_name, command=button_function)
    table_buttons_insert_data_screen.append(button)

back_button = ctk.CTkButton(app, text="Back", command=back_from_insert_data_screen, fg_color="red", hover_color="red4")
table_buttons_insert_data_screen.append(back_button)

#Queries buttons
# Define buttons for each table
queries = {
    "Passenger" : passanger_query,
    "Personnel" : personnel_query,
    "Room" : room_query,
    "Reservation" : reservation_query,
    "Payment" : payment_query
}

queries_screen_buttons = []

for button_name, button_function in queries.items():
    button = ctk.CTkButton(app, text=button_name, command=button_function)
    queries_screen_buttons.append(button)

back_button = ctk.CTkButton(app, text="Back", command=back_from_insert_queries, fg_color="red", hover_color="red4")
queries_screen_buttons.append(back_button)

# Starting the application
app.mainloop()