#!/usr/bin/env python3
"""module for task 7"""
from flask import Flask, render_template, request, g
import pytz
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["fr", "en"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """func to get user"""
    userID = request.args.get("login_as")
    if not userID:
        return None
    for id, user in users.items():
        if id == int(userID):
            return user
    return None


@babel.timezoneselector
def get_timezone():
    """set timezone"""
    timezone = request.args.get("timezone")
    if timezone:
        pytz.timezone(timezone)
        return timezone
    if g.user and g.user.get("timezone"):
        return g.user.get("timezone")
    return Config.BABEL_DEFAULT_TIMEZONE


app.before_request
def before_request():
    """func to get user before request"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """set locale"""
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale
    if g.user:
        user_local = g.user.get("locale")
        if user_local in Config.LANGUAGES:
            return user_local
    locale = request.accept_languages.best_match(app.config["LANGUAGES"])
    if locale:
        return locale
    return Config.BABEL_DEFAULT_LOCALE


@app.route("/")
def oakasan():
    """7-index.html"""
    return render_template("7-index.html", user=g.user)
