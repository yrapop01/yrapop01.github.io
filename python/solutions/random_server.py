"""
    Simple web server which generates random numbers.
"""

from flask import Flask
from flask import request
from flask import render_template
import random

def random_number_generator():
    if (request.method != 'POST' or
        'password' not in request.form or
        request.form['password'] != '2B|!2B'):
            return "Resource is forbidden", 404

    return "Your random number is " + str(random.getrandbits(64))

if __name__ == "__main__":
    app = Flask(__name__)
    app.add_url_rule('/', view_func=random_number_generator,
                     methods=['POST', 'GET'])
    app.run()
