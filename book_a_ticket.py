# Define flight seat availability using a 2D array
flight_a_seats = [[False] * 5 for _ in range(5)]  # 5 rows x 5 seats per row
flight_b_seats = [[False] * 5 for _ in range(5)]



# Function to book a seat
def book_seat(flight_seats):
    try:
        row = int(input("Enter the row number (1-5): ")) - 1
        seat = int(input("Enter the seat number (1-5): ")) - 1

        if 0 <= row < 5 and 0 <= seat < 5:
            if not flight_seats[row][seat]:
                flight_seats[row][seat] = True
                print("Seat booked successfully!")
            else:
                print("Seat already booked. Please select another seat.")
        else:
            print("Invalid row or seat number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a valid row and seat number.")

# Function to display seat availability
def show_seat_availability(flight_seats):
    print("\nSeat Availability:")
    for i, row in enumerate(flight_seats):
        print(f"Row {i + 1}:", " ".join(["X" if seat else "O" for seat in row]))
