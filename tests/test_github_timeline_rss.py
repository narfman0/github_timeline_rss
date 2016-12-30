#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_github_timeline_rss
----------------------------------

Tests for `github_timeline_rss` module.
"""

import json
import unittest
try:
    from unittest import mock
except ImportError:
    from mock import mock

from github_timeline_rss import github_timeline_rss


EXAMPLE = json.loads("""
[
  {
    "id": "12345678",
    "type": "WatchEvent",
    "actor": {
      "id": 1234677,
      "login": "narfman0",
      "display_login": "narfman0",
      "url": "https://api.github.com/users/narfman0"
    },
    "repo": {
      "id": 1234576,
      "name": "narfman0/helga-quip",
      "url": "https://api.github.com/repos/narfman0/helga-quip"
    },
    "payload": {
      "action": "started"
    },
    "public": true,
    "created_at": "2016-12-31T23:59:59Z"
  }
]
""")

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, data):
            self.data = data

        def json(self):
            return self.data

    return MockResponse(EXAMPLE, 200)



class TestGithubTimelineRSS(unittest.TestCase):

    @mock.patch('github_timeline_rss.github_timeline_rss.requests.get', side_effect=mocked_requests_get)
    def setUp(self, mock_requests):
        pass

    def tearDown(self):
        pass

    def test_rssify(self):
        response = github_timeline_rss.feed('narfman0')
        self.assertEquals(response.status_code, 200)
