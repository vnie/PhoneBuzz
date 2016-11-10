from flask import Flask, Response, request
#from twilio import twiml
#import os

app = Flask(__name__)

if __name__ == '__main__':
	port = 5000
	app.run(host='127.0.0.1', port=port, debug=True)


@app.route('/call', methods=['POST'])
def call():
	
