from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, NumberRange

class AddPetForm(FlaskForm):
    """Form to Add Pet"""
    
    name = StringField("Pet's Name", validators=[InputRequired()])
    species = SelectField("Type of Species", 
                          choices=[('cat','cat'),('dog','dog'),('rabbit','rabbit')],
                          validators=[InputRequired()])
    photo_url = StringField("Photo of Pet Link")
    age = IntegerField("Age of pet:",
                       validators=[NumberRange(min=0, max=20)])
    notes = StringField('Additional Notes:')
    available = BooleanField("Available")

