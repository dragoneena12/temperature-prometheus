from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from prometheus_client import CollectorRegistry, make_wsgi_app, Gauge
import RPi.GPIO as GPIO
import dht11
import time
from datetime import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

module = dht11.DHT11(pin=24)

registry = CollectorRegistry()
g = Gauge('dht11', 'dht11', ['kind'], registry=registry)

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.before_request
def before_request():
    while True:
        result = module.read()
        if result.is_valid():
            g.labels('temperature').set(result.temperature)
            g.labels('humidity').set(result.humidity)
            break
        time.sleep(1)

app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    run_simple('172.24.0.4', 8000, app_dispatch, use_reloader=True, use_debugger=True, use_evalex=True)