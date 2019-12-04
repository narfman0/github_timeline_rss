FROM python:alpine

RUN pip install github-timeline-rss

CMD ["github_timeline_rss"]
