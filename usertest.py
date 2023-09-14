import unittest
import json
from app import app  # Import your Flask app

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_crud(self):
        get_response = self.app.get('/api/')
        print(get_response.json)
        self.assertEqual(get_response.status_code, 200)

        new_user = {
            "name": "John Doe"
        }
        create_response = self.app.post('/api/', data=json.dumps(new_user), content_type='application/json')
        print(create_response.json)
        self.assertEqual(create_response.status_code, 201)
    
        user = {
            "name": "John Doe2"
        }
        update_response = self.app.put(f'/api/{create_response.json["id"]}/', data=json.dumps(user), content_type='application/json')
        print(update_response.json)
        self.assertEqual(update_response.status_code, 200)

        delete_response = self.app.delete(f'/api/{create_response.json["id"]}/', content_type='application/json')
        print(delete_response.json)
        self.assertEqual(delete_response.status_code, 200)

if __name__ == '__main__':
    unittest.main()