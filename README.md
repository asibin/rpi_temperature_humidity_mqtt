Temperature / humidity sensor with Raspberry Pi, MQTT and Graphite / Grafana
===

Raspberry Pi (v1) with temperature/humidity sensor (DHT11) sending MQTT messages to MQTT broker while displaying current
temperature and humidity on 2x16 LCD display. 
Includes MQTT subscriber to push MQTT metrics to Graphite / Grafana for easy graphing.

Hardware
---
- Raspberry Pi v1
- Chinese DHT11 temperature / humidity sensor
- Chinese 2x16 LCD display

Prerequisites
---
- Install [Adafruit Python DHT library](https://github.com/adafruit/Adafruit_Python_DHT) on you Raspberry Pi
- Install all the requirements `pip install -r requirements.txt`
- Start mqtt broker (testing only) `docker run -d --name mqtt-broker -p 1883:1883 -p 9001:9001 toke/mosquitto`
- Have Graphite with Grafana installed
- Follow the instructions [here](http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/) to 
enable I2C and find your display address
- `mqtt` and `graphite` are locally resolvable domain names in my case, change them to reflect your settings

TODO
---
- Add TLS
- Buy a better sensor (DHT11 has accuracy of +/- 2 degrees for temperature or +/- 5% for humidity)