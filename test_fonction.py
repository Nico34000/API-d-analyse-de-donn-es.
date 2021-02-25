import unittest

from functions_panda import per_capi, average_year, latest_by_country


class TestMethods(unittest.TestCase):

    def test_by_country(self):
        """Test la fonction latest_by_country."""
        self.assertEqual({'country': 'Albania', 'year': 2017, 'emissions': 4342.011}, latest_by_country('Albania'))
        self.assertIsNotNone({2005}, latest_by_country('France'))
        self.assertIsNot({1999}, latest_by_country('France'))
        self.assertIsInstance(latest_by_country('Belgium'), dict)

       
    def test_average_for_year (self):
        """Test la fonction average_year."""
        self.assertEqual({"total": 217093.22722535214, "year": 2016}, average_year(2016))
        self.assertIsNotNone(1985 ,average_year(1985))
        self.assertIsNotNone({"year": 1975} ,average_year(1975))
        self.assertIsInstance(average_year(1995), dict)
        self.assertIsNot({2000}, average_year(1995))
        
        
if __name__ == '__main__':
    unittest.main()
