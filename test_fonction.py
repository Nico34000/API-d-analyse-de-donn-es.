import unittest

from functions_panda import per_capi, average_year, latest_by_country


class TestMethods(unittest.TestCase):

    def test_by_country(self):
        """Test la fonction latest_by_country."""
        self.assertEqual({'country': 'Albania', 'year': 2017, 'emissions': 4342.011}, latest_by_country('Albania'))
        self.assertIsNotNone({2005}, latest_by_country('France'))
        self.assertIsNot({1999}, latest_by_country('France'))
        self.assertIsInstance(latest_by_country('Belgium'), dict)

if __name__ == '__main__':
    unittest.main()