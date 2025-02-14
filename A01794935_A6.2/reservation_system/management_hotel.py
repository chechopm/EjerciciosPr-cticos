""" This module contains the Management Hotel class. """


from hotel import Hotel


class HotelManagement:
    def __init__(self):
        self.hotels = []
        
    def load_hotels(self):
        """Load the hotels."""
        try:
            with open('reservation_system/data/hotels.txt', 'r') as file:
                for line in file:
                    id, name, city, num_rooms, rooms = line.strip().split(';')
                    rooms = eval(rooms)
                    new_hotel = Hotel(int(id), name, city, int(num_rooms), rooms)
                    self.hotels.append(new_hotel)
            print("Hotels loaded successfully.")
        except FileNotFoundError:
            print("No hotels found.")
        
    def save_hotels(self):
        """Save the hotels."""
        with open('reservation_system/data/hotels.txt', 'w') as file:
            for hotel in self.hotels:
                file.write(f"{hotel.id};{hotel.name};{hotel.city};{hotel.num_rooms};{hotel.rooms}\n")
        print("Hotels saved successfully.")

    def add_hotel(self, name, city, num_rooms):
        """Create a new hotel."""
        id = len(self.hotels) + 1
        new_hotel = Hotel(id, name, city, num_rooms)
        new_hotel.build_rooms()
        self.hotels.append(new_hotel)
        print(f"Hotel '{name}' created successfully whit id {new_hotel.id}.")

    def list_hotels(self):
        """Lists all the hotels."""
        for hotel in self.hotels:
            print(hotel)
        return self.hotels

    def get_hotel_by_id(self, id):
        """Get a hotel by id."""
        if not id.isdigit():
            print(f"Invalid id {id}.")
            return None
        hotel_id = int(id)
        for hotel in self.hotels:
            if hotel.id == hotel_id:
                print(hotel)
                return hotel
        print(f"Hotel with id {id} not found.")
        return None

    def modify_hotel_by_id(self, hotel, new_name=None, new_city=None, new_rooms=None):
        """Modify a hotel."""
        if hotel is None:
            return None
        if new_name:
            hotel.name = new_name
        if new_city:
            hotel.city = new_city
        if new_rooms:
            hotel.num_rooms = int(new_rooms)
            hotel.build_rooms()
        print(f"Hotel '{hotel.name}' modified successfully.")
        print(hotel)
        return hotel
    
    def delete_hotel_by_id(self, hotel):
        """Delete a hotel by id."""
        if hotel is None:
            return None
        self.hotels.remove(hotel)
        print(f"Hotel '{hotel.name}' deleted successfully.")
        return hotel
    
    def reserve_room(self, hotel, customer):
        """Reserve a room."""
        if hotel is None:
            return None
        for room in hotel.rooms:
            if room['status'] == 'available':
                room['status'] = 'reserved'
                room['customer'] = customer
                print(f"Room {room['id']} reserved successfully.")
                return room
        print(f"No rooms available in hotel '{hotel.name}'.")
        return None
    
    def cancel_room(self, hotel, room_id):
        """Cancel a room."""
        if hotel is None:
            return None
        for room in hotel.rooms:
            if int(room['id']) == int(room_id):
                room['status'] = 'available'
                room['customer'] = None
                print(f"Room {room_id} canceled successfully.")
                return room
        print(f"Room {room_id} not found in hotel '{hotel.name}'.")
        return None
