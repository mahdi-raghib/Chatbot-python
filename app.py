import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, jsonify
from rocketchat.api import RocketChatAPI  
from RocketChatBot import RocketChatBot

app = Flask(__name__)

@app.route("/")
def hello():

    api = RocketChatAPI(settings={'username': {os.getenv("ROCKETCHAT_USER")}, 'password': {os.getenv("ROCKETCHAT_PASSWORD")},
    'domain': os.getenv("ROCKETCHAT_URL")})
    #return str(api.get_private_rooms())
    return str(api.get_public_rooms())

    #api.send_message('Hello world!', 'vRRjXCTebcCqR8RFP')


    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')