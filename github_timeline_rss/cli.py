#!/usr/bin/env python
import argparse

from github_timeline_rss.github_timeline_rss import feed


parser = argparse.ArgumentParser(description='Dump github RSS feeds')
parser.add_argument('user', help='Github user from which to ingest timeline')
parser.add_argument('--file', help='Dump to specified file instead of stdout')
args = parser.parse_args()


def main():
    text = feed(args.user).response
    if isinstance(text, list):
        text = b''.join(text)
    if args.file:
        with open(args.file, 'bw') as f:
            f.write(text)
    else:
        print(text)
