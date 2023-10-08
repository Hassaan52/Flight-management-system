#Dictionary to store flight details including arrival and departure times
flight_details = {
    "Flight A": {"arrival_time": "08:00 AM", "departure_time": "12:00 PM"},
    "Flight B": {"arrival_time": "10:30 AM", "departure_time": "02:30 PM"},

}

# Function to manage flight details
def manage_flight_details(flight_name):
    print(f"Manage Details for {flight_name}:")
    print("1. View Details")
    print("2. Modify Arrival Time")
    print("3. Modify Departure Time")
    print("4. Go Back")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print(f"Arrival Time: {flight_details[flight_name]['arrival_time']}")
        print(f"Departure Time: {flight_details[flight_name]['departure_time']}")

    elif choice == '2':
        new_arrival_time = input("Enter new arrival time (e.g., 08:00 AM): ")
        flight_details[flight_name]['arrival_time'] = new_arrival_time
        print(f"Arrival time for {flight_name} updated successfully.")

    elif choice == '3':
        new_departure_time = input("Enter new departure time (e.g., 12:00 PM): ")
        flight_details[flight_name]['departure_time'] = new_departure_time
        print(f"Departure time for {flight_name} updated successfully.")

    elif choice == '4':
        print("Going back to the admin menu.")

    else:
        print("Invalid option. Please select a valid option (1/2/3/4).")


