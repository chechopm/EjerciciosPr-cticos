""" This module contains the Reservation class. """

class Reservation:
    def __init__(self, id, hotel_id, name_hotel, room_id, customer_id, name_customer, status):
        """Initializes the Reservation class."""
        self.id = id
        self.hotel_id = hotel_id
        self.name_hotel = name_hotel
        self.room_id = room_id
        self.customer_id = customer_id
        self.name_customer = name_customer
        self.status = status
        
    def __str__(self):
        return f'ID: {self.id}, Hotel ID: {self.hotel_id}, Name Hotel: {self.name_hotel}, Room ID: {self.room_id}, ID Customer: {self.customer_id}, Name Customer: {self.name_customer}, Status: {self.status}'