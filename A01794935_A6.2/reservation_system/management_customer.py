""" This module contains the Management Customer class. """


from .customer import Customer


class CustomerManagement:
    """This class manages the customers."""
    def __init__(self):
        self.customers = []

    def load_customers(self):
        """Load the customers."""
        try:
            with open(
                'reservation_system/data/customers.txt', 'r', encoding="utf-8"
            ) as file:
                for line in file:
                    (
                        customer_id, name, last_name, nationality
                    ) = line.strip().split(';')
                    new_customer = Customer(
                        customer_id, name, last_name, nationality
                    )
                    self.customers.append(new_customer)
            print("Customers loaded successfully.")
        except FileNotFoundError:
            print("No customers found.")

    def save_customers(self):
        """Save the customers."""
        with open(
            'reservation_system/data/customers.txt',
            'w',
            encoding="utf-8"
        ) as file:
            for customer in self.customers:
                file.write(
                    f"{customer.customer_id};{customer.name};"
                    f"{customer.last_name};{customer.nationality}\n"
                )
        print("Customers saved successfully.")

    def add_customer(self, name, last_name, nationality):
        """Create a new customer."""
        customer_id = len(self.customers) + 1
        new_customer = Customer(customer_id, name, last_name, nationality)
        self.customers.append(new_customer)
        print(
            f"Customer '{name}' created successfully "
            f"whit id {new_customer.customer_id}."
        )

    def list_customers(self):
        """Lists all the customers."""
        for customer in self.customers:
            print(customer)
        return self.customers

    def get_customer_by_id(self, customer_id):
        """Get a customer by id."""
        if not customer_id.isdigit():
            print(f"Invalid id {customer_id}.")
            return None
        customer_id = int(customer_id)
        for customer in self.customers:
            if customer.customer_id == customer_id:
                print(customer)
                return customer
        print(f"Customer with id {customer_id} not found.")
        return None

    def modify_customer_by_id(
        self, customer, new_name=None, new_last_name=None, new_nationality=None
    ):
        """Modify a customer."""
        if customer is None:
            return None
        if new_name:
            customer.name = new_name
        if new_last_name:
            customer.last_name = new_last_name
        if new_nationality:
            customer.nationality = new_nationality
        print(f"Customer '{customer.name}' modified successfully.")
        print(customer)
        return customer

    def delete_customer_by_id(self, customer):
        """Delete a customer by id."""
        if customer is None:
            return None
        self.customers.remove(customer)
        print(f"Customer '{customer.name}' deleted successfully.")
        return customer
