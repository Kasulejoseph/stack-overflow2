from . import app
from flask import Flask, request, jsonify,Response, json

from .data import question

Questions = question()

#get all questions
@app.route('/api/v1/questions/', methods=['GET'])
def questions():
    return jsonify({"questions": Questions})

#get a question
@app.route('/api/v1/questions/<string:id>/', methods=['GET'])
def one_question(id):
    qtn = [question for question in Questions if question['id']== int(id)]
    return jsonify({'question': qtn})

#post a questions
@app.route('/api/v1/questions/', methods=['POST'])
def add_questions():
    data = request.get_json()
    question ={
        "id": data['id'],
        "question": data['question'],
        "author": data['author'],
        "date_created": data['date_created'],
    }
    Questions.append(question)

    return jsonify({'question': Questions})