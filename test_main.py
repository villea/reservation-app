"""Unit tests for the ReservationApp class.

This module contains comprehensive test cases for the ReservationApp class,
testing reservation management functionality including adding reservations,
finding free spots, and checking existing reservations.

Example:
    To run these tests, execute:
        $ python -m unittest test_main.py
"""

import unittest
from main import ReservationApp


class TestReservationApp(unittest.TestCase):
    """Test suite for the ReservationApp class.

    This test suite verifies the functionality of the ReservationApp class,
    including reservation creation, conflict handling, and availability checking.
    """

    def setUp(self):
        """Initialize a fresh ReservationApp instance before each test."""
        self.app = ReservationApp()

    def test_add_reservation_success(self):
        """Test successful reservation creation scenarios.

        Verifies that:
        1. Reservations can be successfully added
        2. Correct reservation data is stored
        3. Adjacent hours are properly handled
        """
        self.assertTrue(self.app.add_reservation("John", 10, 2))
        self.assertEqual(self.app.check_reservation(10), "John")
        self.assertEqual(self.app.check_reservation(11), "John")
        self.assertIsNone(self.app.check_reservation(12))

    def test_add_reservation_conflict(self):
        """Test reservation conflict handling.

        Verifies that:
        1. Overlapping reservations are rejected
        2. Original reservation remains unchanged after conflict
        """
        # Create initial reservation
        self.assertTrue(self.app.add_reservation("John", 10, 2))
        
        # Test overlapping scenarios
        self.assertFalse(self.app.add_reservation("Jane", 10, 1))
        self.assertFalse(self.app.add_reservation("Jane", 11, 1))
        
        # Verify original reservation remains intact
        self.assertEqual(self.app.check_reservation(10), "John")
        self.assertEqual(self.app.check_reservation(11), "John")

    def test_add_reservation_boundary(self):
        """Test boundary conditions for reservations.

        Verifies that:
        1. First hour (0) can be reserved
        2. Last hour (23) can be reserved
        """
        self.assertTrue(self.app.add_reservation("John", 0, 1))
        self.assertTrue(self.app.add_reservation("Jane", 23, 1))
        
        # Verify boundary reservations
        self.assertEqual(self.app.check_reservation(0), "John")
        self.assertEqual(self.app.check_reservation(23), "Jane")

    def test_find_free_spot(self):
        """Test the free spot finding functionality.

        Verifies that:
        1. Empty schedule returns first available slot
        2. Partially filled schedule returns correct available slot
        3. Full schedule returns None
        4. Invalid duration (>24) returns None
        """
        # Test empty schedule
        self.assertEqual(self.app.find_free_spot(4), 0)
        
        # Test partially filled schedule
        self.app.add_reservation("John", 0, 2)
        self.assertEqual(self.app.find_free_spot(4), 2)

        # Test full schedule
        for i in range(0, 24, 2):
            self.app.add_reservation(f"Person{i}", i, 2)
        self.assertIsNone(self.app.find_free_spot(4))

        # Test invalid duration
        self.assertIsNone(self.app.find_free_spot(25))

    def test_check_reservation(self):
        """Test reservation checking functionality.

        Verifies that:
        1. Empty slots return None
        2. Reserved slots return correct name
        3. Multi-hour reservations are properly stored
        """
        # Test empty slot
        self.assertIsNone(self.app.check_reservation(0))
        
        # Test reserved slots
        self.app.add_reservation("John", 0, 2)
        self.assertEqual(self.app.check_reservation(0), "John")
        self.assertEqual(self.app.check_reservation(1), "John")

    def test_add_reservation_invalid_hours(self):
        """Test handling of invalid hour inputs.

        Verifies that:
        1. Negative start hours are handled
        2. Start hours beyond 23 are handled
        3. Negative lengths are handled
        4. Lengths extending beyond 24 are handled
        """
        with self.assertRaises(IndexError):
            self.app.add_reservation("John", -1, 1)
        
        with self.assertRaises(IndexError):
            self.app.add_reservation("John", 24, 1)
        
        with self.assertRaises(IndexError):
            self.app.add_reservation("John", 23, 2)


if __name__ == '__main__':
    unittest.main() 