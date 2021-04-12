import unittest
from Retirement_Tracker import Retire_Tracker
from Retirement_Tracker import The_Hard_Truth

class Retirement_Test_Case(unittest.TestCase):
    def test_Retire_Tracker(self):
        age_met = Retire_Tracker(22, 100000, 0.30, 2000000)
        self.assertEqual(age_met, 89)

    def test_The_Hard_Truth(self):
        success = The_Hard_Truth(80)
        self.assertEqual(success, True)

        success = The_Hard_Truth(99)
        self.assertEqual(success, True)

        success = The_Hard_Truth(100)
        self.assertEqual(success, False)

        success = The_Hard_Truth(110)
        self.assertEqual(success, False)

if __name__ == '__main__':
    unittest.main()
