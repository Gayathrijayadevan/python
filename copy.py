# Initialize bus seats using a dictionary (seat_number: availability)
bus_seats =[]

print("\n1.Registration \n2.Login\n")
a=int(input("enter the choice : "))
if a==1:
        name=input("enter your name : ")
        number=int(input("enter your number : "))
        email=input("enter your email : ")
        password=input("enter your password : ")
        bus_seats.append({"name":name,"number":number,"email":email,"password":password})
elif a==2:
        a=input("\nenter your email :")
        b=input("enter your password :")
        f=0

        while True:
            print("\nWelcome to Seat Reservation System")
            print("1. seat a reservations")
            print("3. Cancel reservation")
            print("4. Quit")
            ch = input("Enter your choice (1-4): ")
            if ch==1:
                print("Current seat reservations:")
                for seat, name in bus_seats.items():
                 print(f"Seat {seat}: {name}")

            elif ch == 2:
                 seat_number = input("Enter seat number to reserve (e.g., A1, B2): ").strip().upper()

                if seat_number in bus_seats:
                    print(f"Seat {seat_number} is already reserved for {bus_seats[seat_number]}")
                else:
                     guest_name = input("Enter guest name: ")
                     bus_seats[seat_number] = guest_name
                     print(f"Seat {seat_number} successfully reserved for {guest_name}")

            elif ch==3:
                    seat_number = input("Enter seat number to cancel reservation: ").strip().upper()

    if seat_number in seat_reservations:
        del seat_reservations[seat_number]
        print(f"Reservation for seat {seat_number} cancelled.")
    else:
        print(f"No reservation found for seat {seat_number}")



while True:
        print("\nBus Seat Reservation System")
        display_seating()
        seat_choice = input("Enter seat number to reserve (or 'q' to quit): ")
        
        if seat_choice.lower() == 'q':
            print("Thank you for using our bus reservation system.")
            break
        
        try:
            seat_number = int(seat_choice)
            reserve_seat(seat_number)
        except ValueError:
            print("Invalid input. Please enter a seat number.")