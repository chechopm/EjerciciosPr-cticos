""" This module contains the Customer class. """

class Customer:
    def __init__(self, id, name, last_name, nationality):
        """Initializes the Customer class."""
        self.id = id
        self.name = name
        self.last_name = last_name
        self.nationality = nationality
        
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Last Name: {self.last_name}, Nationality: {self.nationality}'
