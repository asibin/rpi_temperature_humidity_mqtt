FROM python:2.7-alpine

MAINTAINER Sibin Arsenijevic "sibin.arsenijevic@gmail.com"

ADD . /mqtt-graphite-publisher/

ENV PYTHONPATH /mqtt-graphite-publisher

WORKDIR /mqtt-graphite-publisher

RUN pip install -r requirements.txt

CMD ["python", "mqtt_graphite_publisher.py"]