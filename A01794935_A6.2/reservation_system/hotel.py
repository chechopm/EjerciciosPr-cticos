""" This module contains the Hotel class. """


class Hotel:
    def __init__(self, id, name, city, num_rooms, rooms=[]):
        """Initializes the Hotel class."""
        self.id = id
        self.name = name
        self.city = city
        self.num_rooms = num_rooms
        self.rooms = rooms

    def build_rooms(self):
        """Build the rooms of the hotel."""
        self.rooms = []
        for i in range(1, int(self.num_rooms) + 1):
            self.rooms.append({"id": i, "status": 'available', "customer": None})
    
    def __str__(self):
        """Returns the string representation of the hotel."""
        return f'ID: {self.id}, Name: {self.name}, City: {self.city}, Num Rooms: {self.num_rooms}'
