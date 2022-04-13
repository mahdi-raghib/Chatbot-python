from flask import Flask, jsonify
from pathlib import 
import os
from dotenv import load_dotenv
import time
from rocketchat.api import RocketChatAPI

app = Flask(__name__)

@app.route("/")
def hello():

     api = RocketChatAPI(settings={'username': 'someuser', 'password': 'somepassword',
    'domain': 'https://myrockethchatdomain.com'})


    return jsonify({"Time of Call": time.time()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)