import unittest

from blog import app

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_blog_view(self):
        result = self.app.get("/")
        self.assertIn("Daniel Melo Ramos", result.data.decode("utf-8"))
