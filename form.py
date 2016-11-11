from flask_wtf import Form
from wtforms import TextField, validators

class PhoneForm(Form):
	phone_num_validator = [validators.Required(), validators.regexp(u'[0-9]+')]
	phone_num = TextField('Phone # to call', phone_num_validator)

	def submit(self):
		# Expects 9/10 digit phone numbers i.e
		# 555-555-555 or 1-555-555-555
		if self.phone_num.data != None and (len(self.phone_num.data) == 9 or len(self.phone_num.data) == 10):
			return True
		return False
