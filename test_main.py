import unittest
from main import ReservationApp

class TestReservationApp(unittest.TestCase):
    def setUp(self):
        self.app = ReservationApp()

    def test_add_reservation_success(self):
        # Test successful reservation
        self.assertTrue(self.app.add_reservation("John", 10, 2))
        self.assertEqual(self.app.check_reservation(10), "John")
        self.assertEqual(self.app.check_reservation(11), "John")
        self.assertIsNone(self.app.check_reservation(12))

    def test_add_reservation_conflict(self):
        # Test reservation conflict
        self.app.add_reservation("John", 10, 2)
        self.assertFalse(self.app.add_reservation("Jane", 10, 1))
        self.assertFalse(self.app.add_reservation("Jane", 11, 1))

    def test_add_reservation_boundary(self):
        # Test boundary conditions
        self.assertTrue(self.app.add_reservation("John", 0, 1))  # First hour
        self.assertTrue(self.app.add_reservation("Jane", 23, 1))  # Last hour

    def test_find_free_spot(self):
        # Test finding free spots
        self.assertEqual(self.app.find_free_spot(4), 0)  # Should find first available
        
        # Fill some spots and test again
        self.app.add_reservation("John", 0, 2)
        self.assertEqual(self.app.find_free_spot(4), 2)

        # Test when no spot is available
        for i in range(0, 24, 2):
            self.app.add_reservation(f"Person{i}", i, 2)
        self.assertIsNone(self.app.find_free_spot(4))

    def test_check_reservation(self):
        # Test checking reservations
        self.assertIsNone(self.app.check_reservation(0))
        self.app.add_reservation("John", 0, 2)
        self.assertEqual(self.app.check_reservation(0), "John")
        self.assertEqual(self.app.check_reservation(1), "John")

if __name__ == '__main__':
    unittest.main() 