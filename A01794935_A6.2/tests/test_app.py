import unittest
from unittest.mock import MagicMock, patch
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../reservation_system')))
from reservation_system.app import cancel_reservation

class TestReservationSystem(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_cancel_reservation(self, mock_input):
        # Create mock objects
        mock_management_reservation = MagicMock()
        mock_management_hotel = MagicMock()

        # Set up return values for the mocks
        mock_reservation = MagicMock()
        mock_reservation.hotel_id = 1
        mock_reservation.room_id = 101
        mock_management_reservation.get_reservation_by_id.return_value = mock_reservation
        mock_management_hotel.get_hotel_by_id.return_value = MagicMock()

        # Call the function
        cancel_reservation(mock_management_reservation, mock_management_hotel)

        # Assertions
        mock_management_reservation.get_reservation_by_id.assert_called_once_with('1')
        mock_management_hotel.get_hotel_by_id.assert_called_once_with('1')
        mock_management_hotel.cancel_room.assert_called_once()
        mock_management_reservation.cancel_reservation_by_id.assert_called_once_with(mock_reservation)
        mock_management_reservation.save_reservations.assert_called_once()
        mock_management_hotel.save_hotels.assert_called_once()

if __name__ == '__main__':
    unittest.main()
