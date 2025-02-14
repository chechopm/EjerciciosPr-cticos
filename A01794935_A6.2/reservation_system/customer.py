""" This module contains the Customer class. """


from dataclasses import dataclass


@dataclass
class Customer:
    """This class represents a customer."""
    customer_id: int
    name: str
    last_name: str
    nationality: str

    def __str__(self):
        return (
            f'ID: {self.customer_id}, '
            f'Name: {self.name}, '
            f'Last Name: {self.last_name}, '
            f'Nationality: {self.nationality}'
        )
