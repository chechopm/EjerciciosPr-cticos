""" This module contains the Management Reservation class. """


from reservation import Reservation


class ReservationManagement:
    def __init__(self):
        self.reservations = []
        
    def load_reservations(self):
        """Load the reservations."""
        try:
            with open('reservation_system/data/reservations.txt', 'r') as file:
                for line in file:
                    id, hotel_id, name_hotel, room_id, customer_id, name_customer, status = line.strip().split(';')
                    new_reservation = Reservation(int(id), int(hotel_id), name_hotel, room_id, int(customer_id), name_customer, status)
                    self.reservations.append(new_reservation)
            print("Reservations loaded successfully.")
        except FileNotFoundError:
            print("No reservations found.")
        
    def save_reservations(self):
        """Save the reservations."""
        with open('reservation_system/data/reservations.txt', 'w') as file:
            for reservation in self.reservations:
                file.write(f"{reservation.id};{reservation.hotel_id};{reservation.name_hotel};{reservation.room_id};{reservation.customer_id};{reservation.name_customer};{reservation.status}\n")

    def create_reservation(self, hotel_id, name_hotel, room_id, customer_id, name_customer):
        """Create a new reservation."""
        id = len(self.reservations) + 1
        new_reservation = Reservation(id, hotel_id, name_hotel, room_id, customer_id, name_customer, "active")
        self.reservations.append(new_reservation)
        print(f"Reservation '{id}' created successfully.")
        print(new_reservation)
        
    def get_reservation_by_id(self, id):
        """Get a reservation by id."""
        if not id.isdigit():
            print(f"Invalid id {id}.")
            return None
        reservation_id = int(id)
        for reservation in self.reservations:
            if reservation.id == reservation_id:
                return reservation
        print(f"Reservation '{id}' not found.")
        return None
        
    def cancel_reservation(self, reservation):
        """Cancel a reservation by id."""
        if reservation is None:
            return None
        reservation.status = "cancelled"
        print(f"Reservation '{reservation.id}' cancelled successfully.")
        
    def list_reservations(self):
        """Lists all the reservations."""
        for reservation in self.reservations:
            print(reservation)
        return self.reservations
