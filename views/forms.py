# Form imports
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, DateField


class PredictionForm(FlaskForm):
    team_name     =  StringField('Select Team : ')
    opponent_name =  StringField('Opponent Team : ')
    venue_name    =  PasswordField('Match Venue : ')
    match_date    =  DateField('Match Date : ')
    match_hour    =  IntegerField('Match Hour : ')