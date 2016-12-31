#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_github_timeline_rss
----------------------------------

Tests for `github_timeline_rss` module.
"""

import json
import sys
import unittest
try:
    from unittest import patch
except ImportError:
    from mock import patch

from github_timeline_rss import cli, util


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
    @patch('github_timeline_rss.util.requests.get', side_effect=mocked_requests_get)
    def setUp(self, mock_requests):
        pass

    def test_feed(self):
        response = util.generate_feed('narfman0')
        self.assertEquals(response.status_code, 200)

    def test_cli(self):
        testargs = ["github_timeline_rss", "narfman0"]
        with patch.object(sys, 'argv', testargs):
            cli.main()
