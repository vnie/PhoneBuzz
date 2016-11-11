from flask_wtf import Form
from wtforms import TextField, validators

class PhoneForm(Form):
	phone_num_validator = [validators.Required(), validators.regexp(u'[0-9]+')]
	phone_num = TextField('Phone # to call', phone_num_validator)

	def submit(self):
		# Expects 10 digit phone numbers i.e
		# 555-555-5555
		return self.phone_num.data != None and len(self.phone_num.data) == 9:

