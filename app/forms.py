from flask.ext.wtf import Form, TextField, BooleanField, TextArea, TextAreaField
from flask.ext.wtf import Required

class KeyForm(Form):
  ssh_key = TextAreaField('SSH Key', validators= [Required()])

