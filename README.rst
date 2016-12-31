===============================
Github timeline RSS
===============================


.. image:: https://img.shields.io/pypi/v/github_timeline_rss.svg
        :target: https://pypi.python.org/pypi/github_timeline_rss

.. image:: https://img.shields.io/travis/narfman0/github_timeline_rss.svg
        :target: https://travis-ci.org/narfman0/github_timeline_rss


Github timeline to RSS translation for easier feed integration


* Free software: MIT license


Features
--------

* Create RSS feeds from github timelines
* Command line interface to dump to stdout or a file

Usage
-----

Optional: set up virtualenv environment with::

    virtualenv venv
    source venv/bin/activate

Install requirements::

    pip install -r requirements_dev.txt

Run flask app, e.g.::

    cd github_timeline_rss
    FLASK_APP=rss.py flask run

Test::

    http://127.0.0.1:5000/narfman0

Should show rss feed for activity for narfman0 from github!
