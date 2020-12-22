from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')

class addowner(FlaskForm):
    name=StringField('name of Onwer')
    pup_id=IntegerField('id of puppy')
    submit = SubmitField('add owner')
