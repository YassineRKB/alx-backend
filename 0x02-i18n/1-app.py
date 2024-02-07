#!/usr/bin/env python3
"""module for task 1"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["fr", "en"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def hiMom():
    """1-index.html"""
    return render_template("1-index.html")
