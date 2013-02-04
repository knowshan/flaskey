from flask import Flask
from middleware import RemoteUserMiddleware

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.wsgi_app = RemoteUserMiddleware(app.wsgi_app)
from app import views


