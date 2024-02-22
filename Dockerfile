FROM python:3.7-slim

ENV resume-website=/var/www

ADD . $resume-website
WORKDIR $resume-website

RUN pip install -r $resume-website/requirements.txt