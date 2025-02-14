import unittest
from reservation_system.management_reservation import ReservationManagement

class TestReservationManagement(unittest.TestCase):

    def setUp(self):
        self.reservation_management = ReservationManagement()
        
    def test_load_reservations(self):
        self.reservation_management.load_reservations()
        self.assertEqual(len(self.reservation_management.reservations), 2)
    
    def test_save_reservations(self):
        self.reservation_management.load_reservations()
        self.reservation_management.save_reservations()
        self.assertEqual(len(self.reservation_management.reservations), 2)

    def test_create_reservation(self):
        self.reservation_management.create_reservation(1, "Test Hotel", 1, 1, "Test Customer")
        self.assertEqual(len(self.reservation_management.reservations), 1)
        self.assertEqual(self.reservation_management.reservations[0].hotel_id, 1)
        self.assertEqual(self.reservation_management.reservations[0].name_hotel, "Test Hotel")
        self.assertEqual(self.reservation_management.reservations[0].room_id, 1)
        self.assertEqual(self.reservation_management.reservations[0].customer_id, 1)
        self.assertEqual(self.reservation_management.reservations[0].name_customer, "Test Customer")
        self.assertEqual(self.reservation_management.reservations[0].status, "active")
        self.assertEqual(self.reservation_management.reservations[0].id, 1)
        
    def test_list_reservations(self):
        self.reservation_management.create_reservation(1, "Test Hotel", 1, 1, "Customer One")
        self.reservation_management.create_reservation(1, "Test Hotel", 2, 2, "Customer Two")
        reservations = self.reservation_management.list_reservations()
        self.assertEqual(len(reservations), 2)
        self.assertEqual(reservations[0].hotel_id, 1)
        self.assertEqual(reservations[0].name_customer, "Customer One")
        self.assertEqual(reservations[1].hotel_id, 1)
        self.assertEqual(reservations[1].name_customer, "Customer Two")
            
    def test_get_reservation_by_id(self):
        self.reservation_management.create_reservation(1, "Test Hotel", 1, 1, "Customer One")
        self.reservation_management.create_reservation(1, "Test Hotel", 2, 2, "Customer Two")
        reservation = self.reservation_management.get_reservation_by_id('1')
        self.assertEqual(reservation.name_customer, "Customer One")
        reservation = self.reservation_management.get_reservation_by_id('2')
        self.assertEqual(reservation.name_customer, "Customer Two")
        reservation = self.reservation_management.get_reservation_by_id('3')
        self.assertIsNone(reservation)
        reservation = self.reservation_management.get_reservation_by_id('a')
        self.assertIsNone(reservation)
        
    def test_cancel_reservation(self):
        self.reservation_management.create_reservation(1, "Test Hotel", 1, 1, "Customer One")
        self.reservation_management.create_reservation(1, "Test Hotel", 2, 2, "Customer Two")
        reservation = self.reservation_management.get_reservation_by_id('1')
        self.assertEqual(reservation.status, "active")
        self.reservation_management.cancel_reservation(reservation)
        reservation = self.reservation_management.get_reservation_by_id('1')
        self.assertEqual(reservation.name_customer, "Customer One")
        self.assertEqual(reservation.status, "cancelled")
        
    def test_get_reservation_by_id_invalid(self):
        reservation = self.reservation_management.get_reservation_by_id('a')
        self.assertIsNone(reservation)
        
    def test_cancel_reservation_invalid_reservation(self):
        self.reservation_management.create_reservation(1, "Test Hotel", 1, 1, "Customer One")
        reservation = self.reservation_management.get_reservation_by_id('a')
        self.assertIsNone(reservation)

if __name__ == '__main__':
    unittest.main()