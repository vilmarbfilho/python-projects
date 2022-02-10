from google_play_scraper import app as play_scraper, Sort, reviews
from flask import Flask

import storeconfig as cfg
import json

APPLICATION_ID = cfg.stores["google"]

app = Flask(__name__)

@app.route("/")
def status_api():
    return "api running"

@app.route("/app/details")
def app_details():
    scrap_result = play_scraper(APPLICATION_ID)

    data = {}
    data['installs'] = scrap_result['installs']
    data['minVersion'] = scrap_result['androidVersion']
    data['size'] = scrap_result['size']

    return json.dumps(data)


@app.route("/app/reviews")
def app_reviews():
    result = reviews(
        APPLICATION_ID,
        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
        count=5, # defaults to 100
        filter_score_with=2 # defaults to None(means all score)
    )

    return json.dumps(result, indent=4, sort_keys=True, default=str)