# Weather Data Storage System
weather_records = [] 


# Function to insert a record
def insert_record(date, city, temperature):
    weather_records.append([date, city, temperature])
    print("Record inserted successfully!")


# Function to display all records
def display_records():
    if not weather_records:
        print("No records available.")
        return
    print("\nDate\t\tCity\t\tTemperature")
    print("---------------------------------------")
    for record in weather_records:
        print(f"{record[0]}\t{record[1]}\t\t{record[2]}")


# Function to search records by city
def search_by_city(city):
    found = False
    for record in weather_records:
        if record[1].lower() == city.lower():
            print(f" {record[0]} - {record[1]} - {record[2]}°C")
            found = True
    if not found:
        print(" No records found for this city.")


# Function to delete a record by date + city
def delete_record(date, city):
    for record in weather_records:
        if record[0] == date and record[1].lower() == city.lower():
            weather_records.remove(record)
            print("Record deleted successfully.")
            return
    print(" Record not found.")


#Main Menu 
while True:
    print("\n--- Weather Data Storage System (DSA) ---")
    print("1. Insert Record")
    print("2. Display Records")
    print("3. Search by City")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter Date (DD-MM-YYYY): ")
        city = input("Enter City: ")
        temp = input("Enter Temperature: ")
        insert_record(date, city, temp)

    elif choice == "2":
        display_records()

    elif choice == "3":
        city = input("Enter City Name: ")
        search_by_city(city)

    elif choice == "4":
        date = input("Enter Date of record to delete: ")
        city = input("Enter City of record to delete: ")
        delete_record(date, city)

    elif choice == "5":
        print(" Exiting program. Goodbye!")
        break

    else:
        print(" Invalid choice. Try again.")

