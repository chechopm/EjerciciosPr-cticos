"""Module to run the Reservation System."""


import sys
from .management_hotel import HotelManagement
from .management_customer import CustomerManagement
from .management_reservation import ReservationManagement


def create_hotel(management_hotel):
    """Create a new hotel."""
    name = input("Enter the name of the hotel: ")
    city = input("Enter the city of the hotel: ")
    num_rooms = input("Enter the number of rooms of the hotel: ")
    management_hotel.add_hotel(name, city, num_rooms)
    management_hotel.save_hotels()


def show_hotel(management_hotel):
    """Show a hotel by id."""
    hotel_id = input("Enter the id of the hotel: ")
    management_hotel.get_hotel_by_id(hotel_id)


def modify_hotel(management_hotel):
    """Modify a hotel."""
    hotel_id = input("Enter the id of the hotel: ")
    hotel = management_hotel.get_hotel_by_id(hotel_id)
    if hotel is None:
        return None
    new_name = input(
        "Enter the new name of the hotel "
        "(leave blank to keep current): "
    )
    new_city = input(
        "Enter the new city of the hotel "
        "(leave blank to keep current): "
    )
    new_num_rooms = input(
        "Enter the new number of rooms of the hotel "
        "(leave blank to keep current): "
    )
    management_hotel.modify_hotel_by_id(
        hotel, new_name, new_city, new_num_rooms
    )
    management_hotel.save_hotels()
    return None


def delete_hotel(management_hotel):
    """Delete a hotel by id."""
    hotel_id = input("Enter the id of the hotel: ")
    hotel = management_hotel.get_hotel_by_id(hotel_id)
    if hotel is None:
        return None
    management_hotel.delete_hotel_by_id(hotel)
    management_hotel.save_hotels()
    return None


def create_customer(management_customer):
    """Create a new customer."""
    name = input("Enter the name of the customer: ")
    last_name = input("Enter the last name of the customer: ")
    nationality = input("Enter the nationality of the customer: ")
    management_customer.add_customer(name, last_name, nationality)
    management_customer.save_customers()


def show_customer(management_customer):
    """Show a customer by id."""
    customer_id = input("Enter the id of the customer: ")
    management_customer.get_customer_by_id(customer_id)


def modify_customer(management_customer):
    """Modify a customer."""
    customer_id = input("Enter the id of the customer: ")
    customer = management_customer.get_customer_by_id(customer_id)
    if customer is None:
        return None
    new_name = input(
        "Enter the new name of the customer "
        "(leave blank to keep current): "
    )
    new_last_name = input(
        "Enter the new last name of the customer "
        "(leave blank to keep current): "
    )
    new_nationality = input(
        "Enter the new nationality of the customer "
        "(leave blank to keep current): "
    )
    management_customer.modify_customer_by_id(
        customer, new_name, new_last_name, new_nationality
    )
    management_customer.save_customers()
    return None


def delete_customer(management_customer):
    """Delete a customer by id."""
    customer_id = input("Enter the id of the customer: ")
    customer = management_customer.get_customer_by_id(customer_id)
    if customer is None:
        return None
    management_customer.delete_customer_by_id(customer)
    management_customer.save_customers()
    return None


def create_reservation(
    management_reservation, management_hotel, management_customer
):
    """Create a new customer."""
    hotel_id = input("Enter the id of the hotel: ")
    hotel = management_hotel.get_hotel_by_id(hotel_id)
    if hotel is None:
        return None
    customer_id = input("Enter the id of the customer: ")
    customer = management_customer.get_customer_by_id(customer_id)
    if customer is None:
        return None
    room = management_hotel.reserve_room(hotel, customer.customer_id)
    if room is None:
        return None
    reservation = {
        'hotel_id': hotel_id,
        'name_hotel': hotel.name,
        'room_id': room['room_id'],
        'customer_id': customer_id,
        'name_customer': customer.name
    }
    management_reservation.create_reservation(reservation)
    management_reservation.save_reservations()
    management_hotel.save_hotels()
    return None


def cancel_reservation(management_reservation, management_hotel):
    """Cancel a reservation by id."""
    reservation_id = input("Enter the id of the reservation: ")
    reservation = management_reservation.get_reservation_by_id(reservation_id)
    hotel = management_hotel.get_hotel_by_id(str(reservation.hotel_id))
    management_hotel.cancel_room(hotel, reservation.room_id)
    management_reservation.cancel_reservation(reservation)
    management_reservation.save_reservations()
    management_hotel.save_hotels()


def run_reservation_system(
    management_hotel, management_customer, management_reservation
):
    """Menú Reservation System."""
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        handle_choice(
            choice,
            management_hotel,
            management_customer,
            management_reservation
        )


def print_menu():
    """Print the reservation system menu."""
    print("\nReservation System Menu")
    print("1. Create Hotel")
    print("2. List Hotels")
    print("3. Show Hotel")
    print("4. Modify Hotel")
    print("5. Delete Hotel")
    print("6. Create Customer")
    print("7. List Customers")
    print("8. Show Customer")
    print("9. Modify Customer")
    print("10. Delete Customer")
    print("11. Create Reservation")
    print("12. List Reservations")
    print("13. Cancel Reservation")
    print("0. Exit")


def handle_choice(
    choice, management_hotel, management_customer, management_reservation
):
    """Handle the user's menu choice."""
    choices = {
        '0': sys.exit,
        '1': lambda: create_hotel(management_hotel),
        '2': management_hotel.list_hotels,
        '3': lambda: show_hotel(management_hotel),
        '4': lambda: modify_hotel(management_hotel),
        '5': lambda: delete_hotel(management_hotel),
        '6': lambda: create_customer(management_customer),
        '7': management_customer.list_customers,
        '8': lambda: show_customer(management_customer),
        '9': lambda: modify_customer(management_customer),
        '10': lambda: delete_customer(management_customer),
        '11': lambda: create_reservation(
            management_reservation, management_hotel, management_customer
        ),
        '12': management_reservation.list_reservations,
        '13': lambda: cancel_reservation(
            management_reservation, management_hotel
        )
    }

    action = choices.get(choice)
    if action:
        action()
    else:
        print("Invalid choice. Please try again.")


def main():
    """Principal Main Reservation System."""
    management_hotel = HotelManagement()
    management_hotel.load_hotels()
    management_customer = CustomerManagement()
    management_customer.load_customers()
    management_reservation = ReservationManagement()
    management_reservation.load_reservations()

    run_reservation_system(
        management_hotel, management_customer, management_reservation
    )


if __name__ == "__main__":
    sys.exit(main())
