import unittest
from BMI_Calculator import BMI_Calc
from BMI_Calculator import Get_Category

class BMI_Test_Case(unittest.TestCase):

    def test_BMI_Calc(self):
        BMI = BMI_Calc(6, 0, 160)
        self.assertEqual(BMI, 22.2)

    def test_Get_Category(self):
        category = Get_Category(16.0)
        self.assertEqual(category, "underweight")

        category = Get_Category(18.5)
        self.assertEqual(category, "underweight")

        category = Get_Category(18.6)
        self.assertEqual(category, "a normal weight")

        category = Get_Category(22.0)
        self.assertEqual(category, "a normal weight")

        category = Get_Category(24.9)
        self.assertEqual(category, "a normal weight")

        category = Get_Category(25.0)
        self.assertEqual(category, "overweight")

        category = Get_Category(27.5)
        self.assertEqual(category, "overweight")

        category = Get_Category(29.9)
        self.assertEqual(category, "overweight")

        category = Get_Category(30.0)
        self.assertEqual(category, "obese")

        category = Get_Category(35.0)
        self.assertEqual(category, "obese")

if __name__ == '__main__':
    unittest.main()
