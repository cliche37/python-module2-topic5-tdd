import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(camper_age_input.convert_to_months(10), 120)


if __name__ == '__main__':
    unittest.main()
