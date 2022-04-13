from flask import Flask, jsonify
import time
from rocketchat.api import RocketChatAPI
from rocketchat.calls.chat.send_message import SendMessage

app = Flask(__name__)

@app.route("/")
def hello():

    api = RocketChatAPI(settings={'username': 'hello-world-bot', 'password': '12345678',
    'domain': 'https://chat.milki-psy.dbis.rwth-aachen.de/home'})

    api.send_message('Hello world!', 1111)
    #return jsonify({"Time of Call": time.time()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)