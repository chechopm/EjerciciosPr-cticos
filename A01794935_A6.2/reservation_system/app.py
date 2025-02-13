"""Module to run the Reservation System."""


import sys
from management_hotel import HotelManagement
from management_customer import CustomerManagement


def create_hotel(management_hotel):
    """Create a new hotel."""
    name = input("Enter the name of the hotel: ")
    city = input("Enter the city of the hotel: ")
    num_rooms = input("Enter the number of rooms of the hotel: ")
    management_hotel.add_hotel(name, city, num_rooms)
    management_hotel.save_hotels()


def show_hotel(management_hotel):
    """Show a hotel by id."""
    id = input("Enter the id of the hotel: ")
    management_hotel.get_hotel_by_id(id)


def modify_hotel(management_hotel):
    """Modify a hotel."""
    id = input("Enter the id of the hotel: ")
    hotel = management_hotel.get_hotel_by_id(id)
    if hotel is None:
        return None
    new_name = input("Enter the new name of the hotel (leave blank to keep current): ")
    new_city = input("Enter the new city of the hotel (leave blank to keep current): ")
    new_num_rooms = input("Enter the new number of rooms of the hotel (leave blank to keep current): ")
    management_hotel.modify_hotel_by_id(hotel, new_name, new_city, new_num_rooms)
    management_hotel.save_hotels()

def delete_hotel(management_hotel):
    """Delete a hotel by id."""
    id = input("Enter the id of the hotel: ")
    hotel = management_hotel.get_hotel_by_id(id)
    management_hotel.delete_hotel_by_id(hotel)
    management_hotel.save_hotels()
    
def create_customer(management_customer):
    """Create a new customer."""
    name = input("Enter the name of the customer: ")
    last_name = input("Enter the last name of the customer: ")
    nationality = input("Enter the nationality of the customer: ")
    management_customer.add_customer(name, last_name, nationality)
    management_customer.save_customers()


def show_customer(management_customer):
    """Show a customer by id."""
    id = input("Enter the id of the customer: ")
    management_customer.get_customer_by_id(id)


def modify_customer(management_customer):
    """Modify a customer."""
    id = input("Enter the id of the customer: ")
    customer = management_customer.get_customer_by_id(id)
    if customer is None:
        return None
    new_name = input("Enter the new name of the customer (leave blank to keep current): ")
    new_last_name = input("Enter the new last name of the customer (leave blank to keep current): ")
    new_nationality = input("Enter the new nationality of the customer (leave blank to keep current): ")
    management_customer.modify_customer_by_id(customer, new_name, new_last_name, new_nationality)
    management_customer.save_customers()

def delete_customer(management_customer):
    """Delete a customer by id."""
    id = input("Enter the id of the customer: ")
    customer = management_customer.get_customer_by_id(id)
    management_customer.delete_customer_by_id(customer)
    management_customer.save_customers()

def main():
    """Principal Main Reservation System."""
    management_hotel = HotelManagement()
    management_hotel.load_hotels()
    management_customer = CustomerManagement()
    management_customer.load_customers()

    while True:
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
        
        print("0. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '0':
            print("Exit the program.")
            break

        elif choice == '1':
            create_hotel(management_hotel)

        elif choice == '2':
            management_hotel.list_hotels()

        elif choice == '3':
            show_hotel(management_hotel)

        elif choice == '4':
            modify_hotel(management_hotel)

        elif choice == '5':
            delete_hotel(management_hotel)

        elif choice == '6':
            create_customer(management_customer)
            
        elif choice == '7':
            management_customer.list_customers()
            
        elif choice == '8':
            show_customer(management_customer)

        elif choice == '9':
            modify_customer(management_customer)
            
        elif choice == '10':
            delete_customer(management_customer)

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    sys.exit(main())
