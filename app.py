from flask import Flask, jsonify
from rocketchat.api import RocketChatAPI
#import time
#from rocketchat.calls.chat.send_message import SendMessage
#from rocketchat_API.rocketchat import RocketChat
#from pprint import pprint

app = Flask(__name__)

@app.route("/")
def hello():

    api = RocketChatAPI(settings={'username': 'hello-world-bot', 'password': '12345678',
    'domain': 'https://chat.milki-psy.dbis.rwth-aachen.de/home'})
    
    api.get_private_rooms()

    #api.send_message('Hello world!', 11111)
    #return jsonify({"Time of Call": time.time()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)