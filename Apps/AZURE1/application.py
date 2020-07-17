from flask import Flask
app = Flask(__name__)



#app.send_static_file('indexx.html')

@app.route("/")
def hello():
    return "Hello World!"
