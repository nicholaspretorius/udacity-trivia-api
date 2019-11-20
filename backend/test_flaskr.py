import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from flaskr import create_app
from models import setup_db, Question, Category

load_dotenv()
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format(
            f'{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for
    expected errors.
    """

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        if data['count'] == 0:
            self.assertFalse(data['categories'])
            self.assertFalse(data['count'])
        else:
            self.assertTrue(data['categories'])
            self.assertTrue(data['count'])

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        if data['count'] == 0:
            self.assertFalse(data['questions'])
            self.assertFalse(data['count'])
        else:
            self.assertTrue(data['questions'])
            self.assertTrue(data['count'])

    def test_get_category(self):
        res = self.client().get('/categories/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)

    # def test_get_categories_no_categories(self):
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
