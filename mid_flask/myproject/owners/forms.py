from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name=StringField('name of Owner')
    pup_id=IntegerField('id of puppy')
    submit = SubmitField('add owner')
