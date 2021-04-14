import unittest
from BMICalc import *


class BMITest(unittest.TestCase):

    def test_BMI(self):
        BMI = BMICalc(180,5,7)
        self.assertEqual(BMI,(28.9, 'Average Weight'))

        BMI = BMICalc(200, 4, 0)
        self.assertEqual(BMI,(62.5, 'Overweight'))

        BMI = BMICalc(0,1,0)
        self.assertEqual(BMI,(0s.0, 'Underweight'))

        BMI = BMICalc(150,5,0)
        self.assertEqual(BMI,(30.0, 'Overweight'))

        BMI = BMICalc(150,5,1)
        self.assertEqual(BMI,(29.0,'Average Weight'))

        BMI = BMICalc(180,7,0)
        self.assertEqual(BMI,(18.4, 'Underweight'))

        BMI = BMICalc(181,7,0)
        self.assertEqual(BMI,(18.5, 'Average Weight'))


if __name__ == '__main__':
    unittest.main()