import unittest
from unittest.mock import MagicMock, patch
from io import StringIO
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../reservation_system')))
from reservation_system.app import run_reservation_system, main

class TestReservationSystem(unittest.TestCase):
    
    
    @patch('builtins.input', side_effect=['0'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('management_hotel.HotelManagement')
    @patch('management_customer.CustomerManagement')
    @patch('management_reservation.ReservationManagement')
    def test_main(self, MockHotelManagement, MockCustomerManagement, MockReservationManagement, mock_stdout, mock_input):
        main()


    @patch('builtins.input', side_effect=['1', 'NameTest', 'CityTest', 10, '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_hotel(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_hotel.add_hotel.assert_called_once()


    @patch('builtins.input', side_effect=['2', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_hotels(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_hotel.list_hotels.assert_called_once()        


    @patch('builtins.input', side_effect=['3', '1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_hotel_by_id(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()
        
        mock_hotel = MagicMock()
        mock_management_hotel.get_hotel_by_id.return_value = mock_hotel

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_hotel.get_hotel_by_id.assert_called_once_with('1')


    @patch('builtins.input', side_effect=['4', '1', 'New', 'New', 2, '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_modify_hotel(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()
        
        mock_hotel = MagicMock()
        mock_management_hotel.get_hotel_by_id.return_value = mock_hotel

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_hotel.get_hotel_by_id.assert_called_once_with('1')
        mock_management_hotel.modify_hotel_by_id.assert_called_once_with(mock_hotel, 'New', 'New', 2)


    @patch('builtins.input', side_effect=['4', '1', 'New', 'New', 2, '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_modify_hotel_with_error(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()
        
        mock_management_hotel.get_hotel_by_id.return_value = None

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_hotel.get_hotel_by_id.assert_called_once_with('1')
        mock_management_hotel.modify_hotel_by_id.assert_not_called()


    @patch('builtins.input', side_effect=['5', '1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_hotel(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()
        
        mock_hotel = MagicMock()
        mock_management_hotel.get_hotel_by_id.return_value = mock_hotel

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_hotel.get_hotel_by_id.assert_called_once_with('1')
        mock_management_hotel.delete_hotel_by_id.assert_called_once_with(mock_hotel)


    @patch('builtins.input', side_effect=['6', 'NameTest', 'LastNameTest', 'Nationality', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_customer(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_customer.add_customer.assert_called_once()


    @patch('builtins.input', side_effect=['7', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_customers(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_customer.list_customers.assert_called_once()        


    @patch('builtins.input', side_effect=['8', '1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_customer_by_id(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()
        
        mock_customer = MagicMock()
        mock_management_customer.get_customer_by_id.return_value = mock_customer

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_customer.get_customer_by_id.assert_called_once_with('1')


    @patch('builtins.input', side_effect=['9', '1', 'New', 'New', 'New', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_modify_customer(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()
        
        mock_customer = MagicMock()
        mock_management_customer.get_customer_by_id.return_value = mock_customer

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_customer.get_customer_by_id.assert_called_once_with('1')
        mock_management_customer.modify_customer_by_id.assert_called_once_with(mock_customer, 'New', 'New', 'New')


    @patch('builtins.input', side_effect=['10', '1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_customer(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()
        
        mock_customer = MagicMock()
        mock_management_customer.get_customer_by_id.return_value = mock_customer

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_customer.get_customer_by_id.assert_called_once_with('1')
        mock_management_customer.delete_customer_by_id.assert_called_once_with(mock_customer)


    @patch('builtins.input', side_effect=['11', '1', '1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_reservation(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()
        
        mock_hotel = MagicMock()
        mock_hotel.name = 'Test Hotel'
        mock_hotel.room = [{'id': 1}]
        mock_customer = MagicMock()
        mock_customer.id = 1
        mock_customer.name = 'Test Customer'
        mock_management_hotel.get_hotel_by_id.return_value = mock_hotel
        mock_management_hotel.reserve_room.return_value = mock_hotel.room[0]
        mock_management_customer.get_customer_by_id.return_value = mock_customer
        
        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_hotel.get_hotel_by_id.assert_called_once_with('1')
        mock_management_customer.get_customer_by_id.assert_called_once_with('1')
        mock_management_hotel.reserve_room.assert_called_once_with(mock_hotel, 1)
        mock_management_reservation.create_reservation.assert_called_once_with('1', 'Test Hotel', 1,  '1', 'Test Customer')
        

    @patch('builtins.input', side_effect=['12', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_list_reservations(self, mock_stdout, mock_input):
        mock_management_hotel = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_reservation = MagicMock()

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)

        self.assertIn("Reservation System Menu", mock_stdout.getvalue())
        mock_management_reservation.list_reservations.assert_called_once()


    @patch('builtins.input', side_effect=['13', '1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cancel_reservation(self, mock_stdout, mock_input):
        mock_management_reservation = MagicMock()
        mock_management_customer = MagicMock()
        mock_management_hotel = MagicMock()

        mock_reservation = MagicMock()
        mock_reservation.hotel_id = 1
        mock_reservation.room_id = 101
        mock_management_reservation.get_reservation_by_id.return_value = mock_reservation
        mock_management_hotel.get_hotel_by_id.return_value = MagicMock()

        run_reservation_system(mock_management_hotel, mock_management_customer, mock_management_reservation)
        self.assertIn("Reservation System Menu", mock_stdout.getvalue())

        mock_management_reservation.get_reservation_by_id.assert_called_once_with('1')
        mock_management_hotel.get_hotel_by_id.assert_called_once_with('1')
        mock_management_hotel.cancel_room.assert_called_once()
        mock_management_reservation.cancel_reservation.assert_called_once_with(mock_reservation)
        mock_management_reservation.save_reservations.assert_called_once()
        mock_management_hotel.save_hotels.assert_called_once()

if __name__ == '__main__':
    unittest.main()
