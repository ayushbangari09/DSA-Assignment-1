# Weather Data Storage System using 2D Arrays & ADT

class WeatherRecordADT:
    def __init__(self, max_records=50):
        # 2D Array: Each row = [Date, City, Temperature]
        self.records = [["" for _ in range(3)] for _ in range(max_records)]
        self.size = 0
        self.max_records = max_records

    # Insert new record
    def insert(self, date, city, temperature):
        if self.size >= self.max_records:
            print("Storage is full. Cannot insert new record.")
            return
        self.records[self.size][0] = date
        self.records[self.size][1] = city
        self.records[self.size][2] = temperature
        self.size += 1
        print("Record inserted successfully.")

    # Display all records
    def display(self):
        if self.size == 0:
            print("No weather records available.")
            return
        print("\nStored Weather Records:")
        print("{:<12} {:<15} {:<10}".format("Date", "City", "Temperature"))
        print("-" * 40)
        for i in range(self.size):
            print("{:<12} {:<15} {:<10}".format(
                self.records[i][0],
                self.records[i][1],
                self.records[i][2]
            ))

    # Retrieve records by city
    def retrieve_by_city(self, city):
        found = False
        print(f"\nWeather Records for {city}:")
        for i in range(self.size):
            if self.records[i][1].lower() == city.lower():
                print(f"Date: {self.records[i][0]}, Temp: {self.records[i][2]}")
                found = True
        if not found:
            print("No records found for this city.")

    # Delete record by date and city
    def delete(self, date, city):
        for i in range(self.size):
            if self.records[i][0] == date and self.records[i][1].lower() == city.lower():
                # Shift remaining records up
                for j in range(i, self.size - 1):
                    self.records[j] = self.records[j + 1]
                self.records[self.size - 1] = ["", "", ""]
                self.size -= 1
                print("Record deleted successfully.")
                return
        print("Record not found.")


# --------- Main Program ---------
if __name__ == "__main__":
    system = WeatherRecordADT()

    while True:
        print("\n--- Weather Data Storage System ---")
        print("1. Insert Record")
        print("2. Display All Records")
        print("3. Retrieve Records by City")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            date = input("Enter Date (DD-MM-YYYY): ")
            city = input("Enter City: ")
            temp = input("Enter Temperature: ")
            system.insert(date, city, temp)

        elif choice == "2":
            system.display()

        elif choice == "3":
            city = input("Enter City to Search: ")
            system.retrieve_by_city(city)

        elif choice == "4":
            date = input("Enter Date of Record to Delete: ")
            city = input("Enter City of Record to Delete: ")
            system.delete(date, city)

        elif choice == "5":
            print("Exiting Weather Data Storage System.")
            break

        else:
            print("Invalid choice. Try again.")


