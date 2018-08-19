from flask import Flask
from flask import Flask, request, jsonify,Response, json
from config import app_config


def create_app(config_name):
    from .data import question

    Questions = question()
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_object(app_config["development"])
    

###################
 
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
        response = jsonify({
            "id": data['id'],
            "question": data['question'],
            "author": data['author'],
            "date_created": data['date_created'],
        })
        #Questions.append(question)
        response.status_code = 201
        return response

        return jsonify({'question': Questions})

    #update question
    @app.route('/api/v1/questions/<string:id>/', methods=['PUT'])
    def update_question(id):
        data = request.get_json()
        qtn = [question for question in Questions if question['id']== int(id)]
        question ={
            "id": data['id'],
            "question": data['question'],
            "author": data['author'],
            "date_created": data['date_created'],
            "date_modified": data['date_modified'],
        }
        qtn[0] = question
        return jsonify({'question': qtn[0]})


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


############
    return app
from . import question