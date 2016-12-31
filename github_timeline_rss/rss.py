# -*- coding: utf-8 -*-
""" Entry point for web app """
from flask import Flask

from github_timeline_rss.util import generate_feed


app = Flask(__name__)


@app.route('/<username>')
def feed(username):
    return generate_feed(username)
