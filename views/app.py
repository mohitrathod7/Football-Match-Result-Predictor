import os
from predictor import *
from flask import Flask, request, render_template, jsonify
from forms import PredictionForm


template_dir = os.path.relpath('templates/', 'app.py')
static_dir   = os.path.relpath('static/', 'app.py')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# BASIC CONFIG
app.config['SECRET_KEY'] = 'thisissecret'

@app.errorhandler(404)
def not_found(e):
    return "Page not found"


@app.route('/', methods=["POST", "GET"])
def home():
    form = PredictionForm()

    teams = ['Arsenal', 'Aston Villa', 'Brentford', 'Brighton and Hove Albion', 'Burnley', 'Chelsea', 'Crystal Palace',
             'Everton', 'Fulham', 'Leeds United', 'Leicester City', 'Liverpool', 'Manchester City', 'Manchester United',
             'Newcastle United', 'Norwich City', 'Sheffield United', 'Southampton', 'Tottenham Hotspur', 'Watford',
             'West Bromwich Albion', 'West Ham United', 'Wolverhampton Wanderers']

    if form.validate_on_submit() or request.method == "POST":
        team_name     = form.team_name.data
        opponent_name = form.opponent_name.data
        venue_name    = form.venue_name.data
        match_date    = form.match_date.data
        match_hour    = form.match_hour.data
    
        try:
            predicted_results = predict_new_match_outcome(predictors=predictors+new_cols, team=team_name, opponent=opponent_name, venue=venue_name, date=match_date, hour=match_hour, rf_model=model)
            print(predicted_results)
            
            return jsonify(predicted_results) 
        except Exception as e:
            print(e)

    return render_template("/home.html", teams=teams, form=form)
