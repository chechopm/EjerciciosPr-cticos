""" This module contains the Management Reservation class. """


from .reservation import Reservation


class ReservationManagement:
    """This class manages the reservations."""
    def __init__(self):
        self.reservations = []

    def load_reservations(self):
        """Load the reservations."""
        try:
            with open(
                'reservation_system/data/reservations.txt',
                'r',
                encoding="utf-8"
            ) as file:
                for line in file:
                    (
                        reservation_id,
                        hotel_id,
                        name_hotel,
                        room_id,
                        customer_id,
                        name_customer,
                        status
                    ) = line.strip().split(';')
                    new_reservation = Reservation(
                        reservation_id, int(hotel_id), name_hotel, room_id,
                        int(customer_id), name_customer, status
                    )
                    self.reservations.append(new_reservation)
            print("Reservations loaded successfully.")
        except FileNotFoundError:
            print("No reservations found.")

    def save_reservations(self):
        """Save the reservations."""
        with open(
            'reservation_system/data/reservations.txt', 'w', encoding="utf-8"
        ) as file:
            for reservation in self.reservations:
                file.write(
                    f"{reservation.reservation_id};{reservation.hotel_id};"
                    f"{reservation.name_hotel};{reservation.room_id};"
                    f"{reservation.customer_id};{reservation.name_customer};"
                    f"{reservation.status}\n"
                )

    def create_reservation(self, reservation_details):
        """Create a new reservation."""
        reservation_id = len(self.reservations) + 1
        new_reservation = Reservation(
            reservation_id,
            reservation_details['hotel_id'],
            reservation_details['name_hotel'],
            reservation_details['room_id'],
            reservation_details['customer_id'],
            reservation_details['name_customer'],
            "active"
        )
        self.reservations.append(new_reservation)
        print(f"Reservation '{reservation_id}' created successfully.")
        print(new_reservation)

    def get_reservation_by_id(self, reservation_id):
        """Get a reservation by id."""
        if not reservation_id.isdigit():
            print(f"Invalid id {reservation_id}.")
            return None
        reservation_id = int(reservation_id)
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                return reservation
        print(f"Reservation '{reservation_id}' not found.")
        return None

    def cancel_reservation(self, reservation):
        """Cancel a reservation by id."""
        if reservation is None:
            return None
        reservation.status = "cancelled"
        print(
            f"Reservation '{reservation.reservation_id}' "
            f"cancelled successfully."
        )
        return None

    def list_reservations(self):
        """Lists all the reservations."""
        for reservation in self.reservations:
            print(reservation)
        return self.reservations
