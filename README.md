# PhoneBuzz

App is currently hosted at:
https://damp-sands-51785.herokuapp.com/

Call Twilio #:
+1 626-247-3812


### To run locally

First install the required Python libraries.

`pip install -r requirements.txt`

Set the necessary environment variable(s).

`export TWILIO_AUTH_TOKEN='XXXXXXXXXXXXXXXX'`

To test locally, run a local server/tunnel of your choice. I decided to use ngrok.

`ngrok http 5000`

Start app.

`python run.py`

Then point your Twilio number to the ngrok forwarding URL.

