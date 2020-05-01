from prometheus_client import Gauge, write_to_textfile, REGISTRY
import RPi.GPIO as GPIO
import dht11
import time

TMP_PATH = '/textfile/dht11.prom'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

module = dht11.DHT11(pin=24)

g1 = Gauge('temperature', 'Gauge')
g2 = Gauge('humidity', 'Gauge')

while True:
    result = module.read()
    if result.is_valid():
        g1.set(result.temperature)
        g2.set(result.humidity)
        write_to_textfile(TMP_PATH, REGISTRY)
    time.sleep(1)