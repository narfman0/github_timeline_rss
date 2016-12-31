# -*- coding: utf-8 -*-
from datetime import datetime
import requests
from werkzeug.contrib.atom import AtomFeed


ENDPOINT = 'https://api.github.com/users/{username}/received_events'
TITLE = "{username}'s github timeline"
SUBTITLE = "Timeline as of {date}"
AUTHOR = "{}'s github"
FEED_TITLE = "{} {} {}"
URL = 'https://github.com/{}'


def generate_feed(username):
    title = TITLE.format(username=username)
    url = ENDPOINT.format(username=username)
    subtitle = SUBTITLE.format(date=datetime.now())
    statuses = requests.get(url).json()
    feed = AtomFeed(title, feed_url='/', url='/', subtitle=subtitle)
    for status in statuses:
        event_type = 'starred' if status['type'] == 'WatchEvent' else 'forked'
        user = status['actor']['display_login']
        target = status['repo']['name']
        author = AUTHOR.format(username)
        feed_title = FEED_TITLE.format(user, event_type, target)
        url = URL.format(target)
        date = datetime.strptime(status['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        feed.add(feed_title, "", content_type='html',
                 author=author, url=url, id=status['id'],
                 published=date, updated=date)
    return feed.get_response()
