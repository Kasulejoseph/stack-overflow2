import time, datetime
from flask import Flask, request, jsonify,Response, json
from app import app
from .data import question
date2 = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
Questions = question()
#get all questions
@app.route('/api/v1/questions/', methods=['GET'])
def questions():
    return jsonify({"questions": Questions})

#get a question
@app.route('/api/v1/questions/<string:id>/', methods=['GET'])
def one_question(id):
    for question in Questions:
        if question['id']== int(id):
            return jsonify({'question': question})
    return jsonify({"error": "Error 404 request not found"})
#post a questions
@app.route('/api/v1/questions/', methods=['POST'])
def add_questions():
    data = request.get_json()
    question = {
        "id": data['id'],
        "question": data['question'],
        "author": data['author'],
        "date_created": data['date_created'],
    }

    Questions.append(question)
    response = jsonify(question)
    response.status_code = 201
    return response

#update question
@app.route('/api/v1/questions/<string:id>/', methods=['PUT'])
def update_question(id):
    data = request.get_json()
    if id:
        qtn = [question for question in Questions if question['id']== int(id)]
        quest ={
            "id": data['id'],
            "question": data['question'],
            "author": data['author'],
            "date_created": data['date_created'],
            "date_modified": '{}' .format(date2),
        }
        qtn[0] = quest
        return jsonify({'question': qtn[0]})
    return jsonify({'jkhfh': "id not found"})
#delete question
@app.route('/api/v1/questions/<string:id>/', methods=['DELETE'])
def delete_question(id):
    qtn = [question for question in Questions if question['id']== int(id)]
    Questions.remove(qtn[0])
    return jsonify({'questions': Questions})
#add answer
@app.route('/api/v1/questions/<string:id>/answer', methods=['POST'])
def add_answer(id):
    data = request.get_json()
    qtn = [question for question in Questions if question['id']== int(id)]
    answer = {"answer": data['answer']}
    qtn.append(answer)
    return jsonify({'question': qtn})




