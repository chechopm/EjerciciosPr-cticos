import unittest
from reservation_system.management_customer import CustomerManagement

class TestCustomerManagement(unittest.TestCase):

    def setUp(self):
        self.customer_management = CustomerManagement()
        
    def test_load_customers(self):
        self.customer_management.load_customers()
        self.assertEqual(len(self.customer_management.customers), 1)
    
    def test_save_customers(self):
        self.customer_management.load_customers()
        self.customer_management.save_customers()
        self.assertEqual(len(self.customer_management.customers), 1)

    def test_add_customer(self):
        self.customer_management.add_customer("Test Customer", "Test LastName", "Test Nation")
        self.assertEqual(len(self.customer_management.customers), 1)
        self.assertEqual(self.customer_management.customers[0].name, "Test Customer")
        self.assertEqual(self.customer_management.customers[0].last_name, "Test LastName")
        self.assertEqual(self.customer_management.customers[0].nationality, "Test Nation")
        self.assertEqual(self.customer_management.customers[0].id, 1)

    def test_add_multiple_customers(self):
        self.customer_management.add_customer("Customer One", "LastName One", "Test Nation")
        self.customer_management.add_customer("Customer Two", "LastName Two", "Test Nation")
        self.assertEqual(len(self.customer_management.customers), 2)
        self.assertEqual(self.customer_management.customers[0].name, "Customer One")
        self.assertEqual(self.customer_management.customers[1].name, "Customer Two")
        self.assertEqual(self.customer_management.customers[0].id, 1)
        self.assertEqual(self.customer_management.customers[1].id, 2)
        
    def test_list_customers(self):
        self.customer_management.add_customer("Customer One", "LastName One", "Test Nation")
        self.customer_management.add_customer("Customer Two", "LastName Two", "Test Nation")
        customers = self.customer_management.list_customers()
        self.assertEqual(len(customers), 2)
        self.assertEqual(customers[0].name, "Customer One")
        self.assertEqual(customers[0].last_name, "LastName One")
        self.assertEqual(customers[1].name, "Customer Two")
        self.assertEqual(customers[1].last_name, "LastName Two")
            
    def test_get_customer_by_id(self):
        self.customer_management.add_customer("Customer One", "LastName One", "Test Nation")
        self.customer_management.add_customer("Customer Two", "LastName Two", "Test Nation")
        customer = self.customer_management.get_customer_by_id('1')
        self.assertEqual(customer.name, "Customer One")
        customer = self.customer_management.get_customer_by_id('2')
        self.assertEqual(customer.name, "Customer Two")
        customer = self.customer_management.get_customer_by_id('3')
        self.assertIsNone(customer)
        customer = self.customer_management.get_customer_by_id('a')
        self.assertIsNone(customer)
        
    def test_modify_customer_by_id(self):
        self.customer_management.add_customer("Customer One", "LastName One", "Test Nation")
        self.customer_management.add_customer("Customer Two", "LastName Two", "Test Nation")
        customer = self.customer_management.get_customer_by_id('1')
        self.customer_management.modify_customer_by_id(customer, new_name="New Customer", new_last_name="New Last Name", new_nationality="New City")
        self.assertEqual(customer.name, "New Customer")
        self.assertEqual(customer.last_name, "New Last Name")
        self.assertEqual(customer.nationality, "New City")
        self.customer_management.modify_customer_by_id(customer, new_name="New Customer")
        self.assertEqual(customer.name, "New Customer")
        self.customer_management.modify_customer_by_id(customer, new_last_name="New Last Name")
        self.assertEqual(customer.last_name, "New Last Name")
        self.customer_management.modify_customer_by_id(customer, new_nationality="New City Two")
        self.assertEqual(customer.nationality, "New City Two")
        
    def test_delete_customer_by_id(self):
        self.customer_management.add_customer("Customer One", "LastName One", "Test Nation")
        self.customer_management.add_customer("Customer Two", "LastName Two", "Test Nation")
        customer = self.customer_management.get_customer_by_id('1')
        self.customer_management.delete_customer_by_id(customer)
        self.assertEqual(len(self.customer_management.customers), 1)
        self.assertEqual(self.customer_management.customers[0].name, "Customer Two")    
        
    def test_get_customer_by_id_invalid(self):
        customer = self.customer_management.get_customer_by_id('a')
        self.assertIsNone(customer)
        
    def test_delete_customer_by_invalid_id(self):
        self.customer_management.add_customer("Customer One", "City One", 5)
        customer = self.customer_management.get_customer_by_id('a')
        self.assertIsNone(customer)

if __name__ == '__main__':
    unittest.main()