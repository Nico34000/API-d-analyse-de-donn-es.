import unittest
from api import app

class TestApiFlask(unittest.TestCase):


    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 


    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200) 


    def test_home_by_country(self):
        result = self.app.get('/latest_by_country/Albania')
        self.assertEqual(result.status_code, 200) 
        self.assertTrue(b'country'in result.data)
        self.assertEqual(result.content_type,'application/json')
        result_2 = self.app.get('/latest_by_country/Aania')
        self.assertEqual(result_2.status_code, 404)




















if __name__ == '__main__':
    unittest.main()