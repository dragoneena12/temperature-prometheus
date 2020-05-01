from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from prometheus_client import make_wsgi_app, Counter

c = Counter('my_counter', 'Description of access counter')

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.before_request
def before_request():
    c.inc()

app_dispatch = DispatcherMiddleware(app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    run_simple('localhost', 8000, app_dispatch, use_reloader=True, use_debugger=True, use_evalex=True)