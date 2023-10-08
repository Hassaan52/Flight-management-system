
# Function to add a new flight
def add_flight(flight_name):
    global flight_a_seats, flight_b_seats
    if flight_name == "Flight A":
        flight_a_seats = [[False] * 5 for _ in range(5)]
    elif flight_name == "Flight B":
        flight_b_seats = [[False] * 5 for _ in range(5)]
    # Add more flights here if needed

# Function to modify a flight
def modify_flight(flight_name):
    global flight_a_seats, flight_b_seats
    if flight_name == "Flight A":
        flight_a_seats = [[False] * 5 for _ in range(5)]
    elif flight_name == "Flight B":
        flight_b_seats = [[False] * 5 for _ in range(5)]

# Function to remove a flight
def remove_flight(flight_name):
    global flight_a_seats, flight_b_seats
    if flight_name == "Flight A":
        flight_a_seats = []
    elif flight_name == "Flight B":
        flight_b_seats = []


# Function to show admin menu
def show_admin_menu():
    while True:
        print("\nWelcome Admin")
        print("1. Add a Flight")
        print("2. Modify a Flight")
        print("3. Remove a Flight")
        print("4. Logout")
        choice = input("Please select an option (1/2/3/4): ")

        if choice == '1':
            flight_name = input("Enter the name of the new flight: ")
            add_flight(flight_name)
            print(f"Flight {flight_name} added successfully.")

        elif choice == '2':
            flight_name = input("Enter the name of the flight to modify: ")
            modify_flight(flight_name)
            print(f"Flight {flight_name} modified successfully.")

        elif choice == '3':
            flight_name = input("Enter the name of the flight to remove: ")
            remove_flight(flight_name)
            print(f"Flight {flight_name} removed successfully.")

        elif choice == '4':
            print("Logging out as admin...")
            break

        else:
            print("Invalid option. Please select a valid option (1/2/3/4).")
