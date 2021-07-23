import unittest

from app import main


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["current_uri"], "/")
        self.assertIn("resources_uris", data)

    def test_users_page(self):
        response = self.app.get('/users', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_specific_user(self):
        response = self.app.get('/users/geralt', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            "description": "Traveling monster slayer for hire",
            "name":"Geralt of Rivia"
        })



if __name__ == '__main__':
    unittest.main()
