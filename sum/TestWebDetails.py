import unittest
import sumapp
import json

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.app = sumapp.app.test_client()

    def test_status_code(self):
        response = self.app.get('/details')
        self.assertEquals(response.status_code, 200)

    def test_status_response_type(self):
        response = self.app.get('/details')
        self.assertIsInstance(json.loads(response.get_data()), dict)

    def test_status_response_values(self):
        response = self.app.get('/details')
        result = json.loads(response.get_data())
        self.assertEquals({'IP', 'Date'} - set(result.keys()), set())
