from . import app
from flask import Flask, request, jsonify,Response, json

from .data import question

Questions = question()

#get all questions
@app.route('/api/v1/questions/', methods=['GET'])
def questions():
    return jsonify({"questions": Questions})

