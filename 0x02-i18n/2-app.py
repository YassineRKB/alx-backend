#!/usr/bin/env python3
"""module for task 2"""
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
    local = request.accept_languages.best_match(app.config["LANGUAGES"])
    return local


@app.route("/")
def hiMom():
    """2-index.html"""
    return render_template("2-index.html")
