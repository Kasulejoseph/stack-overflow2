import time
import datetime
date2 = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
def question():
    questions = [
        {
            "id": 1,
            "question": "Copying a cell from a selected range of columns to a specific column while keeping the same row",
            "author": "kasul",
            "date_created": '{}' .format(date2),
            "answers": 6,
        },
         {
            "id": 2,
            "question": "how to capture the spaces in regular expression?",
            "author": "erick",
            "date_created": '{}' .format(date2),
            "answers": 4,
        },
         {
            "id": 3,
            "question": "how to capture the spaces in regular expression?",
            "author": "nicholas",
            "date_created": '{}' .format(date2),
            "answers": 2,
        },
         {
            "id": 4,
            "question": " Trying to select a variable from within a ForEach loop, and if that variable is less than a certain number, display another variable as Red",
            "author": "emanuel",
            "date_created": '{}' .format(date2),
            "answers":0,
        },
        {
            "question": "this my test",
            "id":10,
        }
    ]
    return questions
