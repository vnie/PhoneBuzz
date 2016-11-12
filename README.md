# PhoneBuzz

App is currently hosted at:
https://damp-scrubland-52655.herokuapp.com
However, the Twilio # attached cannot call numbers it has not added to its list verified caller IDs.


### To run locally

First install the required Python libraries.

`pip install -r requirements.txt`

Set the necessary environment variable(s).

```
export TWILIO_AUTH_TOKEN='XXXXXXXXXXXXXXXX'
export TWILIO_ACCOUNT_SID='XXXXXXXXXXXXXXX'
export TWILIO_PHONE_NUMBER='XXXXXXXXXXXXXX'
export SECRET_KEY='ANYTHING'
```

To test locally, run a local server/tunnel of your choice. I decided to use ngrok.

`ngrok http 5000`

Start up app.

`python run.py`
