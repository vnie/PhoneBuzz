from flask import Flask, Response, request
from twilio import twiml
#from twilio.util import RequestValidator

#***REMOVED***
#validator = RequestValidator(AUTH_TOKEN)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def call():
	''' Handles incoming calls '''
	resp = twiml.Response()
	with resp.gather(timeout=5, action="/handle-input", finishOnKey="#", method="POST") as g:
		g.say("Hi, please enter your FizzBuzz number and then press pound")
	
	return str(resp)


@app.route("/handle-input", methods=['POST'])
def handle_input():
	''' Handles user input ''' 
	
	resp = twiml.Response()
	
	try:
		n = int(request.values.get('Digits', None))		
		if n < 1:
			return redirect("/")

		resp.say(_fizzbuzz(n))
	except:
		resp.say("ENTER A SMALLER NUMBER DUDE")

	return str(resp)
	

def _fizzbuzz(n):
	result = [""] * n
	for i in range(1, n+1):
		if i%3 == 0:
			result[i-1] += "Fizz"
		if i%5 == 0:
			result[i-1] += "Buzz"
		if i%3 != 0 and i%5 != 0:
			result[i-1] += str(i)
	return ", ".join(result)

if __name__ == '__main__':
	#port = 5000
	#app.run(host='127.0.0.1', port=port, debug=True)
	app.run()
