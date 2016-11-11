from flask import Flask, Response, request, abort, render_template
from twilio import twiml
from twilio.rest import TwilioRestClient
from twilio.util import RequestValidator
import phonenumbers
import form
import os

TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER', None)
SECRET_KEY = os.environ.get('SECRET_KEY', None)
URL = "https://damp-scrubland-52655.herokuapp.com"

app = Flask(__name__)
app.config.update(SECRET_KEY=SECRET_KEY)

@app.route("/", methods=['GET', 'POST'])
def call():
	phone_form = form.PhoneForm()

	if phone_form.submit():
		phone_num = phonenumbers.format_number(phonenumbers.parse(phone_form.phone_num.data, 'US'),
											   phonenumbers.PhoneNumberFormat.NATIONAL)

		# Make call
		client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
		try:
			call = client.calls.create(to=phone_num, from_=TWILIO_PHONE_NUMBER, url=URL+"/call")
			return render_template('confirmation.html')
		except:
			pass
		
	return render_template('index.html')


@app.route("/call", methods=['GET', 'POST'])
def get_input():
	''' Handles incoming calls '''
#	validator = RequestValidator(TWILIO_AUTH_TOKEN)
#	signature = request.headers.get('X-Twilio-Signature', '')
#	
#	if not validator.validate(request.url, request.form, signature):
#		return abort(403)

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
	port = int(os.environ.get("PORT", 5000))
	#app.run(host='127.0.0.1', port=port, debug=True)
	app.run(port=port)
