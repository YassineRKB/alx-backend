#!/usr/bin/env python3
"""module for task 0"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def heyMom():
    """0-index.html"""
    return render_template("0-index.html")
