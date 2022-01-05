from google_play_scraper import app as play_scraper
from flask import Flask

app = Flask(__name__)

@app.route("/")
def status_api():
    return "api running"

@app.route("/app/details")
def app_details():
    return play_scraper("applicationId") 