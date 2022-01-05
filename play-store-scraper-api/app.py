from google_play_scraper import app as play_scraper
from flask import Flask

app = Flask(__name__)

@app.route("/")
def statusApi():
    return "api running"

@app.route("/app/detail")
def detail():
    return play_scraper("applicationId") 