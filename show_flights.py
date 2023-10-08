# Function to display all flights
def show_all_flights():
    print("Flight List:")
    print("1. Flight A")
    print("2. Flight B")


# Function to show seat availability
def show_seat_availability(flight_seats):
    print("\nSeat Availability:")
    for i, row in enumerate(flight_seats):
        print(f"Row {i + 1}:", " ".join(["X" if seat else "O" for seat in row]))
