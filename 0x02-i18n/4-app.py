#!/usr/bin/env python3
"""module for task 4"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["fr", "en"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """set locale"""
    local = request.args.get("locale")
    if local in Config.LANGUAGES:
        return local
    else:
        local = request.accept_languages.best_match(app.config["LANGUAGES"])
    return local


@app.route("/")
def helloMother():
    """4-index.html"""
    return render_template("4-index.html")
