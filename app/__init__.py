#This file will initialize the flask app, configure settings and load other components like
# routes, data, preprocessing, models, etc.

from flask import Flask 
app = Flask(__name__) #initializing flask app
app.config.from_object('app.config') #importing app config settings
from app import routes