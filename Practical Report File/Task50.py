import mysql.connector

def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="SHOPPING_LIST"
    )
    return connection

def insert_item(connection):
    cursor = connection.cursor()
    item_id = input("Enter Item ID: ")
    item_name = input("Enter Item Name: ")
    item_cost = input("Enter Item Cost: ")
    item_quantity = input("Enter Item Quantity: ")
    query = "INSERT INTO ITEMS (item_id, item_name, item_cost, item_quantity) VALUES (%s, %s, %s, %s)"
    values = (item_id, item_name, item_cost, item_quantity)
    cursor.execute(query, values)
    connection.commit()
    print("Item inserted successfully.")

def remove_item(connection):
    cursor = connection.cursor()
    item_id = input("Enter Item ID to remove: ")
    query = "DELETE FROM ITEMS WHERE item_id = %s"
    values = (item_id,)
    cursor.execute(query, values)
    connection.commit()
    print("Item removed successfully.")

def modify_item(connection):
    cursor = connection.cursor()
    item_id = input("Enter Item ID to modify: ")
    item_name = input("Enter new Item Name: ")
    item_cost = input("Enter new Item Cost: ")
    item_quantity = input("Enter new Item Quantity: ")
    query = "UPDATE ITEMS SET item_name = %s, item_cost = %s, item_quantity = %s WHERE item_id = %s"
    values = (item_name, item_cost, item_quantity, item_id)
    cursor.execute(query, values)
    connection.commit()
    print("Item modified successfully.")

def search_item(connection):
    cursor = connection.cursor()
    item_id = input("Enter Item ID to search: ")
    query = "SELECT * FROM ITEMS WHERE item_id = %s"
    values = (item_id,)
    cursor.execute(query, values)
    items = cursor.fetchall()
    if not items:
        print("Item not found.")
    else:
        for item in items:
            print("Item ID:", item[0])
            print("Item Name:", item[1])
            print("Item Cost:", item[2])
            print("Item Quantity:", item[3])
            print()

def display_items(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM ITEMS"
    cursor.execute(query)
    items = cursor.fetchall()
    if not items:
        print("No items found.")
    else:
        for item in items:
            print("Item ID:", item[0])
            print("Item Name:", item[1])
            print("Item Cost:", item[2])
            print("Item Quantity:", item[3])
            print()

def menu():
    connection = connect_to_database()
    while True:
        print("\nMenu:")
        print("1. Insert item")
        print("2. Remove item")
        print("3. Modify item")
        print("4. Search item")
        print("5. Display items")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            insert_item(connection)
        elif choice == '2':
            remove_item(connection)
        elif choice == '3':
            modify_item(connection)
        elif choice == '4':
            search_item(connection)
        elif choice == '5':
            display_items(connection)
        elif choice == '6':
            connection.close()
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
