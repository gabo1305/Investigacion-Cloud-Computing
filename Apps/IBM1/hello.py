from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
import atexit
import os
import json

app = Flask(__name__, static_url_path='')





port = int(os.getenv('PORT', 8000))

@app.route('/')
def root():
##    n=5
##    factorial_total = 1
##    while n > 1:
##        factorial_total *= n
##        n -= 1
##    return str(factorial_total)

    return app.send_static_file('index.html')



@app.route('/')
def factorial():
    n=5
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
