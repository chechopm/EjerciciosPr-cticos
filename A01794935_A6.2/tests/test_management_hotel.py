import unittest
from reservation_system.management_hotel import HotelManagement

class TestHotelManagement(unittest.TestCase):

    def setUp(self):
        self.hotel_management = HotelManagement()
        
    def test_load_hotels(self):
        self.hotel_management.load_hotels()
        self.assertEqual(len(self.hotel_management.hotels), 2)
    
    def test_save_hotels(self):
        self.hotel_management.load_hotels()
        self.hotel_management.save_hotels()
        self.assertEqual(len(self.hotel_management.hotels), 2)

    def test_add_hotel(self):
        self.hotel_management.add_hotel("Test Hotel", "Test City", 10)
        self.assertEqual(len(self.hotel_management.hotels), 1)
        self.assertEqual(self.hotel_management.hotels[0].name, "Test Hotel")
        self.assertEqual(self.hotel_management.hotels[0].city, "Test City")
        self.assertEqual(self.hotel_management.hotels[0].num_rooms, 10)
        self.assertEqual(self.hotel_management.hotels[0].id, 1)

    def test_add_multiple_hotels(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        self.hotel_management.add_hotel("Hotel Two", "City Two", 15)
        self.assertEqual(len(self.hotel_management.hotels), 2)
        self.assertEqual(self.hotel_management.hotels[0].name, "Hotel One")
        self.assertEqual(self.hotel_management.hotels[1].name, "Hotel Two")
        self.assertEqual(self.hotel_management.hotels[0].id, 1)
        self.assertEqual(self.hotel_management.hotels[1].id, 2)
        
    def test_list_hotels(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        self.hotel_management.add_hotel("Hotel Two", "City Two", 15)
        hotels = self.hotel_management.list_hotels()
        self.assertEqual(len(hotels), 2)
        self.assertEqual(hotels[0].name, "Hotel One")
        self.assertEqual(hotels[0].city, "City One")
        self.assertEqual(hotels[1].name, "Hotel Two")
        self.assertEqual(hotels[1].city, "City Two")
            
    def test_get_hotel_by_id(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        self.hotel_management.add_hotel("Hotel Two", "City Two", 15)
        hotel = self.hotel_management.get_hotel_by_id('1')
        self.assertEqual(hotel.name, "Hotel One")
        hotel = self.hotel_management.get_hotel_by_id('2')
        self.assertEqual(hotel.name, "Hotel Two")
        hotel = self.hotel_management.get_hotel_by_id('3')
        self.assertIsNone(hotel)
        hotel = self.hotel_management.get_hotel_by_id('a')
        self.assertIsNone(hotel)
        
    def test_modify_hotel_by_id(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        self.hotel_management.add_hotel("Hotel Two", "City Two", 15)
        hotel = self.hotel_management.get_hotel_by_id('1')
        self.hotel_management.modify_hotel_by_id(hotel, new_name="New Hotel", new_city="New City", new_rooms=10)
        self.assertEqual(hotel.name, "New Hotel")
        self.assertEqual(hotel.city, "New City")
        self.assertEqual(hotel.num_rooms, 10)
        self.hotel_management.modify_hotel_by_id(hotel, new_name="New Hotel")
        self.assertEqual(hotel.name, "New Hotel")
        self.hotel_management.modify_hotel_by_id(hotel, new_city="New City")
        self.assertEqual(hotel.city, "New City")
        self.hotel_management.modify_hotel_by_id(hotel, new_rooms=5)
        self.assertEqual(hotel.num_rooms, 5)
        
    def test_delete_hotel_by_id(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        self.hotel_management.add_hotel("Hotel Two", "City Two", 15)
        hotel = self.hotel_management.get_hotel_by_id('1')
        self.hotel_management.delete_hotel_by_id(hotel)
        self.assertEqual(len(self.hotel_management.hotels), 1)
        self.assertEqual(self.hotel_management.hotels[0].name, "Hotel Two")    
    
    def test_reserve_room(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        hotel = self.hotel_management.get_hotel_by_id('1')
        room = self.hotel_management.reserve_room(hotel, "Test Customer")
        self.assertEqual(room['status'], 'reserved')
        self.assertEqual(room['customer'], 'Test Customer')
        
    def test_cancel_room(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        hotel = self.hotel_management.get_hotel_by_id('1')
        room = self.hotel_management.reserve_room(hotel, "Test Customer")
        self.hotel_management.cancel_room(hotel, room['id'])
        self.assertEqual(room['status'], 'available')
        self.assertIsNone(room['customer'])
        
    def test_get_hotel_by_id_invalid(self):
        hotel = self.hotel_management.get_hotel_by_id('a')
        self.assertIsNone(hotel)
        
    def test_delete_hotel_by_invalid_id(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        hotel = self.hotel_management.get_hotel_by_id('a')
        self.assertIsNone(hotel)
        
    def test_reserve_room_no_hotel(self):
        room = self.hotel_management.reserve_room(None, "Test Customer")
        self.assertIsNone(room)
            
    def test_reserve_room_no_rooms(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 0)
        hotel = self.hotel_management.get_hotel_by_id('1')
        room = self.hotel_management.reserve_room(hotel, "Test Customer")
        self.assertIsNone(room)
            
    def test_reserve_room_some_reserved(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 5)
        hotel = self.hotel_management.get_hotel_by_id('1')
        hotel.rooms[0]['status'] = 'reserved'
        room = self.hotel_management.reserve_room(hotel, "Test Customer")
        self.assertEqual(room['status'], 'reserved')
        self.assertEqual(room['customer'], 'Test Customer')
        
    def test_cancel_room_no_hotel(self):
        room = self.hotel_management.cancel_room(None, None)
        self.assertIsNone(room)
        
    def test_cancel_room_no_rooms(self):
        self.hotel_management.add_hotel("Hotel One", "City One", 0)
        hotel = self.hotel_management.get_hotel_by_id('1')
        room = self.hotel_management.cancel_room(hotel, None)
        self.assertIsNone(room)

if __name__ == '__main__':
    unittest.main()