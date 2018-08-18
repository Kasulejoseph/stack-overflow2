from . import app
from flask import Flask, request, jsonify,Response, json

from .data import question

Questions = question()

#get all questions
@app.route('/api/v1/questions/', methods=['GET'])
def questions():
    return jsonify({"questions": Questions})

<<<<<<< HEAD
#get a question
@app.route('/api/v1/questions/<string:id>/', methods=['GET'])
def one_question(id):
    qtn = [question for question in Questions if question['id']== int(id)]
    return jsonify({'question': qtn})

=======
>>>>>>> get_all_questions
