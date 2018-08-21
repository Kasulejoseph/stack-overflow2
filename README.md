
# stack overflow-lite API
This app allows a user to ask questions or get answers using APIs

# Build Status

 [![Build Status](https://travis-ci.com/Kasulejoseph/stack-overflow2.svg?branch=master)](https://travis-ci.com/Kasulejoseph/stack-overflow2)   [![Coverage Status](https://coveralls.io/repos/github/Kasulejoseph/stack-overflow2/badge.svg?branch=master)](https://coveralls.io/github/Kasulejoseph/stack-overflow2?branch=master)     [![Maintainability](https://api.codeclimate.com/v1/badges/200e88c979824a569d0a/maintainability)](https://codeclimate.com/github/Kasulejoseph/stack-overflow2/maintainability)

# Getting Started
A user can do the following with the app
* Get all questions. 
* Get a question. 
* Post a question.
* delete a question. 
* update a question.  
* Post an answer to a question. 

# Built-with
```
   - Python3.5 - Programming language that is more convienient to develop with
   - Flask - A most powerful Python web framework
   - Virtualenv - A tool to create isolated virtual environment
   - Pytest - python web testing frame work
   - pylint
  ```

# installation procedures
This is a step by step procedure of this app running successfully on your machine

Ensure you have **Python** installed by entering ```python --v``` on your terminal. If you don't have **Python** installed go to the [Python Website](https://www.python.org/), and follow the download instructions.

## Clone this Repository
``` $ https://github.com/Kasulejoseph/stack-overflow2
    $ cd stack-overflow2
```
## Install virtual environment and activate it
``` $ pip install virtualenv
    $ virtualenv env -to create virtual environment
    $ source env/bin/activate -- to activate the virtual environment
```
## In the virtual environment install Flask
``` $ pip install flask ```

## Now run the app server by
``` $ python run.py ```

## Running the automated tests
from the root folder of the application run 
``` $ python -m unittest discover ```
## Test running routes
|Method | End-Point | Functionality|
| ---| --- | ---|
| POST |api/v1/questions/ | User post a question. |
| GET |api/v1/questions/id | User get one question. |
| PUT |api/v1/questions/id | User updates a question. |
| GET |api/v1/questions/ | User get all questions. |
| DELETE |api/v1/questions/id | User delete a question he posted. |
| POST |api/v1/questions/id/answer | User post an answer to a question. |

## Author 
**Kasule Joseph**
 
## Acknowlegments
**Nalubega Joyce**
**team oopia**

 
