import mysql.connector
from mysql.connector import Error

Hotel_fields = ['ID', 'Name', 'Age', 'Address', 'Country', 'Email', 'Mobile', 'Checkin_date', 'Checkout_date', 'Room_number', 'Room_rent', 'Restaurant_bill', 'Laundry_bill', 'Gaming_bill', 'Total_bill']

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mannan@123"
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

# Main program starts here
host = "localhost"
user = "root"
password = "Mannan@123"

connection = create_server_connection(host, user, password)

# Create a new database
create_db_query = "CREATE DATABASE IF NOT EXISTS HotelManagement"
create_database(connection, create_db_query)

# Connect to the newly created database
db_connection = mysql.connector.connect(
    host=host,
    user=user,
    passwd=password,
    database="HotelManagement"
)

# Create a table within the database
create_table_query = """
CREATE TABLE IF NOT EXISTS Customers (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Age INT,
    Address VARCHAR(255),
    Country VARCHAR(100),
    Email VARCHAR(100),
    Mobile VARCHAR(20),
    Checkin_date DATE,
    Checkout_date DATE,
    Room_number INT,
    Room_rent DECIMAL(10, 2),
    Restaurant_bill DECIMAL(10, 2),
    Laundry_bill DECIMAL(10, 2),
    Gaming_bill DECIMAL(10, 2),
    Total_bill DECIMAL(10, 2)
);
"""
execute_query(db_connection, create_table_query)


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Mannan@123",
        database="HotelManagement"
    )

def add_customer():
    db = connect_db()
    cursor = db.cursor()

    print("-------------------------")
    print("Add Customer Information")
    print("-------------------------")

    customer_data = {}
    fields = ['Name', 'Age', 'Address', 'Country', 'Email', 'Mobile', 'Checkin_date', 'Checkout_date', 'Room_number']
    for field in fields:
        customer_data[field] = input(f"Enter {field}: ")

    print("\n ***** We have The Following Rooms For You *****")
    print(" 1. Studio -----> Rs.10000")
    print(" 2. Elite -----> Rs.5000 ")
    print(" 3. Double -----> Rs.3500 ")
    print(" 4. Single -----> Rs.2500  \n")

    room_choice = int(input("Enter Your Choice Please->"))
    no_of_days = int(input("Number of nights: "))
    room_rent = [10000, 5000, 3500, 2500][room_choice - 1] * no_of_days

    customer_data['Room_rent'] = room_rent
    customer_data['Restaurant_bill'] = 0
    customer_data['Laundry_bill'] = 0
    customer_data['Gaming_bill'] = 0
    customer_data['Total_bill'] = room_rent  # Initial total bill is just the room rent

    placeholders = ', '.join(['%s'] * len(customer_data))
    columns = ', '.join(customer_data.keys())
    sql = "INSERT INTO Customers (%s) VALUES (%s)" % (columns, placeholders)
    cursor.execute(sql, list(customer_data.values()))
    db.commit()

    # Retrieve and show the new customer's ID
    customer_id = cursor.lastrowid
    print(f"\nData saved successfully. Customer ID is: {customer_id}")
    input("\nPress any key to continue")

    cursor.close()
    db.close()

def restaurant_bill():
    db = connect_db()
    cursor = db.cursor()

    ID = int(input("Enter your ID: "))
    print("\n*****RESTAURANT MENU*****\n")
    print("1.water----->Rs.10 \n2.tea----->Rs15 \n3.breakfast combo-->Rs1150 \n4.lunch---->Rs900 \n5.dinner--->Rs1200 \n6.Exit\n")

    choice = int(input("Enter your choice: "))
    if choice == 6:
        cursor.close()
        db.close()
        return
    
    quantity = int(input("Enter the quantity: "))
    prices = {1: 10, 2: 15, 3: 1150, 4: 900, 5: 1200}
    rtbill = quantity * prices.get(choice, 0)
    print("Total Food Cost=Rs", rtbill, "\n")

    sql = """
        UPDATE Customers 
        SET Restaurant_bill = Restaurant_bill + %s,
            Total_bill = Total_bill + %s
        WHERE ID = %s
    """
    cursor.execute(sql, (rtbill, rtbill, ID))
    db.commit()

    cursor.close()
    db.close()
    print(input('\nPress any key to continue'))


def laundry_bill():
    db = connect_db()
    cursor = db.cursor()

    ID = input('Enter Customer ID: ')
    print("\n******LAUNDRY MENU*******\n")
    print("1.Shorts----->Rs3 \n2.Trousers----->Rs4 \n3.Shirt--->Rs5 \n4.Jeans---->Rs6 \n5.Girlsuit--->Rs8 \n6.Exit\n")

    laundry = int(input("Enter your choice: "))
    if laundry == 6:
        cursor.close()
        db.close()
        return

    quantity = int(input("Enter the quantity: "))
    prices = {1: 3, 2: 4, 3: 5, 4: 6, 5: 8}
    lbill = quantity * prices.get(laundry, 0)
    print("Your Total Laundry Bill=Rs", lbill, "\n")

    sql = """
        UPDATE Customers 
        SET Laundry_bill = Laundry_bill + %s,
            Total_bill = Total_bill + %s
        WHERE ID = %s
    """
    cursor.execute(sql, (lbill, lbill, ID))
    db.commit()

    cursor.close()
    db.close()
    print(input('\nPress any key to continue'))

def gaming_bill():
    db = connect_db()
    cursor = db.cursor()

    ID = int(input("Enter your ID: "))
    print("\n******GAMING MENU*******\n")
    print("1. Table Tennis -----> 150 Rs./HOURS \n2. Bowling -----> 100 Rs./HOURS \n3. Sight of the Serpent ----> 250 Rs./HOURS \n4. Karting ----> 400 Rs./HOURS \n5. Video Games -----> 300 Rs./HOURS \n6. Swimming Pool Games-----> 350 Rs./HOURS \n7. Exit\n")

    game = int(input("Enter The Game You Want To Play: "))
    if game == 7:
        cursor.close()
        db.close()
        return

    hour = int(input("Enter No. Of Hours You Want To Play: "))
    prices = {1: 150, 2: 100, 3: 250, 4: 400, 5: 300, 6: 350}
    gamingbill = hour * prices.get(game, 0)

    sql = """
        UPDATE Customers 
        SET Gaming_bill = Gaming_bill + %s,
            Total_bill = Total_bill + %s
        WHERE ID = %s
    """
    cursor.execute(sql, (gamingbill, gamingbill, ID))
    db.commit()

    cursor.close()
    db.close()
    print(input('\nPress any key to continue'))

def search():
    db = connect_db()
    cursor = db.cursor()

    Name = input('Enter Customer Name You Want To Search: ')
    sql = "SELECT * FROM Customers WHERE Name LIKE %s"
    cursor.execute(sql, ("%"+Name+"%",))
    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print('No Customer Data Found!')

    cursor.close()
    db.close()
    print(input('\nPress any key to continue'))

def total_bill():
    db = connect_db()
    cursor = db.cursor()

    ID = input('Enter Customer ID: ')
    sql = "SELECT * FROM Customers WHERE ID = %s"
    cursor.execute(sql, (ID,))
    result = cursor.fetchone()

    if result:
        print("\n******HOTEL BILL******")
        for field, value in zip(Hotel_fields, result):
            print(f'{field}: {value}')
    else:
        print("No such customer!")

    cursor.close()
    db.close()
    input('\nPress any key to continue')


def main_menu():
    while True:
        print("""
        1--->Enter Customer Details
        2--->Calculate Restaurant Bill
        3--->Calculate Laundry Bill
        4--->Calculate Game Bill
        5--->Search Customer
        6--->Generate Total Bill
        7--->Exit
        """)

        choice = input("Enter Your Choice: ")
        if choice == '1':
            add_customer()
        elif choice == '2':
            restaurant_bill()
        elif choice == '3':
            laundry_bill()
        elif choice == '4':
            gaming_bill()
        elif choice == '5':
            search()
        elif choice == '6':
            total_bill()
        elif choice == '7':
            print("Thank you for using our system!")
            break
        else:
            print("Invalid Choice. Please choose again.")

if __name__ == '__main__':
    main_menu()
