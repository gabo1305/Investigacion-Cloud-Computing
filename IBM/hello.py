from flask import Flask
import os

app = Flask(__name__)

port=int(os.getenv("VCAP_APP_PORT")

@app.route('/')
def hello_wold():
  return "hello world" I am runnin in port:"+str(port)
 if __name__=='main':
  app.run(host='0.0.0.0',port=port)
