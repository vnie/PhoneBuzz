# PhoneBuzz

App is currently hosted at 

First install the required Python libraries.

`pip install -r requirements.txt`

Set the necessary environment variable(s).

`export TWILIO_AUTH_TOKEN='XXXXXXXXXXXXXXXX'`

To test locally, run a local server/tunnel of your choice. I decided to use ngrok.

`ngrok http 5000`

Then point your Twilio number to the ngrok forwarding URL.

