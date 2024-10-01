import pickle
import pandas as pd
import numpy as np


# Load the trained model and variables from the .pkl file
with open('C:/Users/mohit/OneDrive/Desktop/later/data/Football_Match_Win_Prediction/models/model_variables.pkl', 'rb') as v:
    matches_rolling, rolling_averages = pickle.load(v)

with open('C:/Users/mohit/OneDrive/Desktop/later/data/Football_Match_Win_Prediction/models/model.pkl', 'rb') as f:
    model = pickle.load(f)

    
predictors = ["venue_code", "opp_code", "hour", "day_code"]
cols = ["gf", "ga", "sh", "sot", "dist", "fk", "pk", "pkatt"]
new_cols = [f"{c}_rolling" for c in cols]


def predict_new_match_outcome(team, opponent, venue, date, hour, rf_model, predictors):
    team_data = matches_rolling[matches_rolling["team"] == team]
    team_data = team_data.groupby("team").apply(lambda x: rolling_averages(x, cols, new_cols))
    
    if team_data.index.nlevels > 1:
        team_data = team_data.droplevel(level=0)
    
    team_data.index = range(team_data.shape[0])

    gf_rolling    = team_data["gf_rolling"].iloc[-1]
    ga_rolling    = team_data["ga_rolling"].iloc[-1]
    sh_rolling    = team_data["sh_rolling"].iloc[-1]
    sot_rolling   = team_data["sot_rolling"].iloc[-1]
    dist_rolling  = team_data['dist_rolling'].iloc[-1]
    fk_rolling    = team_data["fk_rolling"].iloc[-1]
    pk_rolling    = team_data["pk_rolling"].iloc[-1]
    pkatt_rolling = team_data["pkatt_rolling"].iloc[-1]

    new_match = pd.DataFrame({
        'team':     [team],
        'opponent': [opponent],
        'venue':    [venue],
        'time':     ['{hour}:00'.format(hour=hour)],

        'date':     [pd.to_datetime(date)],
        'gf':       [np.nan],
        'ga':       [np.nan],
        'sh':       [np.nan],
        'sot':      [np.nan],
        'dist':     [np.nan],
        'fk':       [np.nan],
        'pk':       [np.nan],
        'pkatt':    [np.nan],

        'gf_rolling':    [gf_rolling],
        'ga_rolling':    [ga_rolling],
        'sh_rolling':    [sh_rolling],
        'sot_rolling':   [sot_rolling],
        'dist_rolling':  [dist_rolling],
        'fk_rolling':    [fk_rolling],
        'pk_rolling':    [pk_rolling],
        'pkatt_rolling': [pkatt_rolling]
    })

    new_match["venue_code"] = new_match["venue"].astype("category").cat.codes
    new_match["opp_code"]   = new_match["opponent"].astype("category").cat.codes
    new_match["hour"]       = new_match["time"].str.replace(":.+", "", regex=True).astype("int")
    new_match["day_code"]   = new_match["date"].dt.dayofweek

    prediction    = rf_model.predict(new_match[predictors])
    probabilities = rf_model.predict_proba(new_match[predictors])

    return{
        'prediction':            int(prediction[0]),
        'win_probability':       round(float(probabilities[0][1]*100), 2),
        'loss_draw_probability': round(float(probabilities[0][0]*100), 2),
    }
