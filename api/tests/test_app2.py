import unittest

from main import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_home(self):
        response = self.client.post("/", data={"content": "hello world"})
        assert response.status_code == 200
        assert "POST method called" == response.get_data(as_text=True)

if __name__ == "__main__":
    unittest.main()