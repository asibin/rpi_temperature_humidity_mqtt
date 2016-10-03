import logging

import Adafruit_DHT
import paho.mqtt.client as mqtt
import I2C_LCD_driver

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

mylcd = I2C_LCD_driver.lcd()

mqttc = mqtt.Client("dht11_publisher")
mqttc.connect("mqtt", 1883)
mqttc.loop_start()

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4, delay_seconds=10, retries=5)

    if humidity is not None or temperature is not None:

        mqttc.publish("iot/home/sensors/livingroom/temperature", temperature, retain=True)
        mqttc.publish("iot/home/sensors/livingroom/humidity", humidity, retain=True)

        mylcd.lcd_display_string("Temp: %d%s C" % (temperature, chr(223)), 1)
        mylcd.lcd_display_string("Humidity: %d %%" % humidity, 2)

        LOG.info('Temp: %s C  Humidity: %s %%', temperature, humidity)
