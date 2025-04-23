# test fixtures

# Checkpoint 1
import unittest
import kiosk


class CheckInKioskTests(unittest.TestCase):

  def test_check_in_with_flight_number(self):
    print('Testing the check-in process based on flight number')

  def test_check_in_with_passport(self):
    print('Testing the check-in process based on passport')

  # Checkpoint 2
  @classmethod
  def setUpClass(cls):
    kiosk.power_on_kiosk()
    
  # Checkpoint 3
  @classmethod
  def tearDownClass(cls):
    kiosk.power_off_kiosk()
    
  # Checkpoint 4
  def setUp(self):
    kiosk.return_to_welcome_page()

unittest.main()
