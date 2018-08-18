import unittest
import os
import json
from . import app
class QuestionTestCase(unittest.TestCase):
    """This class represents the question test case"""
    
    def setUp(self):
        """  """
        self.app = app()
        self.qtn = self.app.test_client
        self.question = {'question': 'what is the most used programing language?'}

    def test_api_can_get_all_questions(self):
        """Test API can get a questions (GET request)."""
        # res = self.qtn().post('/app/v1/questions', data=self.question)
        # self.assertEqual(res.status_code, 201)
        res = self.qtn().get('/app/v1/questions')
        self.assertEqual(res.status_code, 200)
        self.assertIn('what is the most used', str(res.data))

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()