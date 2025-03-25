import unittest
from app import create_app, db
from app.models import User

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        response = self.client.get('/bp/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    def test_users_page(self):
        with self.app.app_context():
            db.session.add(User(name="Test User", email="test@example.com"))
            db.session.commit()

        response = self.client.get('/bp/users')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test User", response.data)

if __name__ == '__main__':
    unittest.main()
