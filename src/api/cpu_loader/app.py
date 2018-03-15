import logging

from flask import Flask
from werkzeug.wsgi import DispatcherMiddleware

from cpu_loader.application import Application


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
application = Application()
application.register(app)


def simple(env, resp):
    resp('404 NOT FOUND', [('mimetype', 'application/json')])
    return [b'']


app.wsgi_app = DispatcherMiddleware(simple, {'/api': app.wsgi_app})


if __name__ == '__main__':
    app.run()

