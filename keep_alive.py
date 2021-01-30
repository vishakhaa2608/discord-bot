from flask import Flask
from threading import Thread

"""
    This flask app will act as Bot's web server.
    Uptime Robot is set to ping the bot's web server on heroku every 5 minutes. 
    With constant pings, the bot will never enter the sleeping stage and will just keep running.
"""
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello. I am alive!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
