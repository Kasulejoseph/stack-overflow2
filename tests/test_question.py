from flask import url_for, request
import unittest
import os
import json
import sys
from app import create_app
from flask import current_app
class QuestionTestCase(unittest.TestCase):
    """This class represents the question test case"""
    
    def setUp(self):
        """  """
        self.app = create_app("testing")
        self.qtn = self.app.test_client
        self.app_context = self.app.app_context()
        self.client = self.app.test_client(use_cookies=True)
        self.app_context.push()
        self.question = {  
            "answers": 2,
            "author": "erick",
            "date_created": "04-05-2018",
            "id": 12,
            "question": "how to capture the spaces in regular expression?"
            }
   
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertFalse(current_app.config['TESTING'])

    def test_question_creation(self):
        """Test API can create a question (POST request)"""
        res = self.client.post('/api/v1/questions/',
        content_type='application/json', data=json.dumps(self.question) )
        self.assertEqual(res.status_code, 201)

    def test_api_can_get_question_by_id(self):
        """Test API can get a single bucketlist by using it's id."""
        rv = self.client.post('/api/v1/questions/',
        content_type='application/json', data=json.dumps(self.question) )
        self.assertEqual(rv.status_code, 201)

        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client.get('/api/v1/questions/{}/'.format(result_in_json['id']),
         content_type='application/json',
           data=json.dumps(self.question))

        self.assertEqual(result.status_code, 200)

    def test_api_can_get_all_questions(self):
        """Test API can get a questions (GET request)."""
        res = self.client.post('/api/v1/questions/',
        content_type='application/json', data=json.dumps(self.question) )
        self.assertEqual(res.status_code, 201)

        res = self.client.get('/api/v1/questions/', content_type='application/json',
           data=json.dumps(self.question))
        self.assertEqual(res.status_code, 200)

    # def test_delete_question(self):
    #     """Test API can delete an existing question. (DELETE request)."""
    #     rv = self.client.post('http://localhost:5000/api/v1/questions/',
    #     content_type='application/json', data=json.dumps(self.question) )
    #     self.assertEqual(rv.status_code, 201)

    #     result = self.client.delete('http://localhost:5000/api/v1/questions/app/v1/questions/')
    #     self.assertEqual(result.status_code, 200)
    #     # Test to see if it exists, should return a 404
    #     result = self.client.get('http://localhost:5000/api/v1/questions/app/v1/questions/1')
    #     self.assertEqual(result.status_code, 404)

    def test_question_can_be_edited(self):
        """Test API can edit an existing question. (PUT request)"""
        rv = self.client.post('/api/v1/questions/',
        content_type='application/json', data=json.dumps(self.question) )
        self.assertEqual(rv.status_code, 201)
        # edit question
        rv = self.client.put(
            '/api/v1/questions/1/', content_type='application/json',
            data = json.dumps({
            "date_modified": "9/07/2003",
            "author": "ericko",
            "date_created": "04-25-2012",
            "id": 12,
            "question": "How to capture the spaces in regular expression?"
            }))
        self.assertEqual(rv.status_code, 200)
        # results = self.client.get('http://localhost:5000/api/v1/questions/1/')

    # def test_can_add_answer_to_question(self):
    #     """Test API can add an answer to the question (POST request)."""
    #     res = self.client.post('http://localhost:5000/api/v1/questions/',
    #     content_type='application/json', data=json.dumps(self.question) )
    #     self.assertEqual(res.status_code, 201)

    #     result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
    #     result = self.client.get('http://localhost:5000/api/v1/questions/{}/'.format(result_in_json['id']),
    #      content_type='application/json',
    #        data=json.dumps(self.question))

    #     self.assertEqual(result.status_code, 200)

    #     result = self.client.put('http://localhost:5000/api/v1/questions/1/answer', 
    #      content_type='application/json',
    #         data = json.dumps({
    #         "answer": "2",
    #         "author": "ericko",
    #         "date_created": "04-25-2012",
    #         "id": 12,
    #         "question": "How to capture the spaces in regular expression?"
    #         },
    #         {"answer": "this is the answer to thw question?"}
    #         ))
            
    #     self.assertEqual(result.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()