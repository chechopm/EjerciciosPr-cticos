""" This module contains the Reservation class. """


from dataclasses import dataclass


@dataclass
class Reservation:
    """This class represents a reservation."""
    reservation_id: int
    hotel_id: int
    name_hotel: str
    room_id: int
    customer_id: int
    name_customer: str
    status: str

    def __str__(self):
        return (
            f'ID: {self.reservation_id}, '
            f'Hotel ID: {self.hotel_id}, '
            f'Name Hotel: {self.name_hotel}, '
            f'Room ID: {self.room_id}, '
            f'ID Customer: {self.customer_id}, '
            f'Name Customer: {self.name_customer}, '
            f'Status: {self.status}'
        )
