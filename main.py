#usernames and passwords
from admin_interface import show_admin_menu
from book_a_ticket import show_seat_availability, book_seat, flight_a_seats, flight_b_seats
from cancel_booking import cancel_booking
from show_flights import show_all_flights

user_credentials = {'client1': 'abc', 'client2': 'xyz'}
admin_credentials = {'admin': 'admin123'}

# Function to check if the input credentials
def is_valid_user(username, password):
    return username in user_credentials and user_credentials[username] == password


def is_valid_admin(username, password):
    return username in admin_credentials and admin_credentials[username] == password

# Function to show the user menu
def show_user_menu(username):
    while True:
        print("\nUser Menu for", username)
        print("1. Book a Ticket")
        print("2. Cancel a Booking")
        print("3. Show Available Flights")
        print("4. Logout")
        choice = input("Please select an option (1/2/3/4): ")

        if choice == '1':
            print("Booking a ticket...")
            print("Select a flight:")
            print("1. Flight A")
            print("2. Flight B")
            flight_choice = input("Enter your choice (1/2): ")

            if flight_choice == '1':
             print("Seat availability for Flight A:")
             show_seat_availability(flight_a_seats)
             book_seat(flight_a_seats)
            elif flight_choice == '2':
             print("Seat availability for Flight B:")
             show_seat_availability(flight_b_seats)
             book_seat(flight_b_seats)
            else:
             print("Invalid choice. Please select a valid flight.")

        elif choice == '2':
             print("Canceling a booking...")
             print("Enter your username to cancel your booking:")
             cancel_username = input("Username: ")
             print("Select a flight:")
             print("1. Flight A")
             print("2. Flight B")
             flight_choice = input("Enter your choice (1/2): ")

             if flight_choice == '1':
                flight_name = "Flight A"
                flight_seats = flight_a_seats
             elif flight_choice == '2':
                flight_name = "Flight B"
                flight_seats = flight_b_seats
             else:
                print("Invalid choice. Please select a valid flight.")
                continue

             print("Seat availability for", flight_name)
             show_seat_availability(flight_seats)
             row = int(input("Enter the row number (1-5): ")) - 1
             seat = int(input("Enter the seat number (1-5): ")) - 1

             if 0 <= row < 5 and 0 <= seat < 5:
              if flight_seats[row][seat]:
               cancel_booking(cancel_username, flight_name, row, seat)
              else:
               print("Seat is not booked by this user.")
             else:
              print("Invalid row or seat number. Please try again.")

        elif choice == '3':
            print("Showing available flights...")
            show_all_flights()
            flight_choice = input("Enter the flight number to see seat availability: ")

            if flight_choice == '1':
               print("Seat availability for Flight A:")
               show_seat_availability(flight_a_seats)
            elif flight_choice == '2':
               print("Seat availability for Flight B:")
               show_seat_availability(flight_b_seats)
            else:
               print("Invalid choice. Please select a valid flight.")

        elif choice == '4':
            print("Logging out...")
            break

        else:
            print("Invalid option. Please select a valid option (1/2/3/4).")

#main code
while True:
    print("Welcome to the Simple Login System")
    print("1. User Login")
    print("2. Admin Login")
    print("3. Exit")
    choice = input("Please select an option (1/2/3): ")

    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if is_valid_user(username, password):
            print("Login successful! Welcome, User:", username)
            show_user_menu(username)
        else:
            print("Invalid credentials. Please try again.")

    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if is_valid_admin(username, password):
            show_admin_menu();
            print("Login successful! Welcome, Admin:", username)
        else:
            print("Invalid credentials. Please try again.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option (1/2/3).")
