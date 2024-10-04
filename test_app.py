# tests/test_app.py
import unittest
from app import app  # Import your Flask app

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        # Set up a test client for your Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test the home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Replace 'Welcome' with actual content

    def test_not_found(self):
        # Test a non-existent page
        response = self.app.get('/non-existent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
