""" This module contains the Hotel class. """

from dataclasses import dataclass


@dataclass
class Hotel:
    """This class represents a hotel."""
    hotel_id: int
    name: str
    city: str
    num_rooms: int
    rooms: list = None

    def build_rooms(self):
        """Build the rooms of the hotel."""
        self.rooms = []
        for i in range(1, int(self.num_rooms) + 1):
            self.rooms.append(
                {
                    "room_id": i,
                    "status": 'available',
                    "customer": None
                }
            )

    def __str__(self):
        """Returns the string representation of the hotel."""
        return (
            f'ID: {self.hotel_id}, '
            f'Name: {self.name}, '
            f'City: {self.city}, '
            f'Num Rooms: {self.num_rooms}'
        )
