from flask import url_for, request

import unittest
import os,json,sys,datetime, time
from app import app
from flask import current_app
class QuestionTestCase(unittest.TestCase):
    """This class represents the question test case"""
    
    def setUp(self):
        """ initatializing tests """
        self.date2 = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
        self.app_context = app.app_context()
        self.client = app.test_client(use_cookies=True)
        self.app_context.push()
        self.question = {  
            "answers": 2,
            "author": "erick",
            "date_created": '{}' .format(self.date2),
            "id": 1,
            "question": "how to capture the spaces in regular expression?"
            }
    
    def test_app_exists(self):
        "test if app exists"
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        "test if testing is activated or working"
        self.assertFalse(current_app.config['TESTING'])

    def test_question_creation(self):
        """Test API can create a question (POST request)"""
        result = self.client.post('/api/v1/questions/',
        content_type='application/json', data=json.dumps(self.question) )
        author ='"author": "erick"'
        self.assertEqual(result.status_code, 201)
        self.assertIn(author, str(result.data))

    def test_api_can_get_question_by_id(self):
        """Test API can get a single question by using it's id."""
        rv = self.client.post('/api/v1/questions/',
        content_type='application/json', data=json.dumps(self.question) )
        self.assertEqual(rv.status_code, 201)

        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client.get('/api/v1/questions/3/',
         content_type='application/json',
           data=json.dumps(self.question))
    
        id ='{}' .format(result_in_json['id'])
        self.assertEqual(result.status_code, 200)
        self.assertIn(id, str(result.data))

    def test_api_can_get_all_questions(self):
        """Test API can get a questions (GET request)."""
        res = self.client.post('/api/v1/questions/',
        content_type='application/json', data=json.dumps(self.question) )
        self.assertEqual(res.status_code, 201)

        res = self.client.get('/api/v1/questions/', content_type='application/json',
           data=json.dumps(self.question))
        author ='"author": "erick"'
        self.assertEqual(res.status_code, 200)
        self.assertIn(author, str(res.data))

    def test_question_can_be_edited(self):
        """Test API can edit an existing question. (PUT request)"""
        rv = self.client.post('/api/v1/questions/',
        content_type='application/json', data=json.dumps(self.question) )
        self.assertEqual(rv.status_code, 201)
        # edit question
        rv = self.client.put(
            '/api/v1/questions/2/', content_type='application/json',
            data = json.dumps({
            "date_modified": '{}' .format(self.date2),
            "author": "erick",
            "date_created": "04-25-2012",
            "id": 1,
            "question": "How to capture the spaces in regular expression?"
            }))
        self.assertEqual(rv.status_code, 200)
        # get new edit
        author = '"author": "erick"'
        rx = self.client.get('http://localhost:5000/api/v1/questions/2/')
        self.assertEqual(rx.status_code, 200)
        self.assertIn(author, str(rx.data))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()