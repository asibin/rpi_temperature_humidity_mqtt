"""Subscribes to all 'iot' topics and publishes them to Graphite with 'mqtt' prefixed"""

import time
import logging

import graphitesend
import paho.mqtt.client as mqtt


logging.basicConfig(level=logging.INFO, format="[%(asctime)s][%(levelname)s] - %(message)s")
LOG = logging.getLogger(__name__)

CARBON_SERVER = 'graphite'
CARBON_PORT = 2003
PREFIX = 'mqtt'

graphitesend.init(graphite_server=CARBON_SERVER,
                  graphite_port=CARBON_PORT,
                  prefix=PREFIX,
                  system_name='')


def on_connect(client, userdata, flags, rc):
    LOG.info("Connected with result code %s", str(rc))
    client.subscribe("iot/#")


def on_message(client, userdata, msg):
    topic = msg.topic.replace('/', '.')
    message = "mqtt.{} {} {}".format(topic, str(msg.payload.decode()), time.time())

    LOG.debug("Sending:\t%s", message)

    graphitesend.send(topic, str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt", 1883, 60)

client.loop_forever()
