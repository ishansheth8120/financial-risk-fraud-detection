#This file defines the routes for the webapp. Handling requests and integrating front end with the backend 

from flask import render_template, request, redirect, url_for
from app import app
from app.data_loader import load_data
from app.models import predict_fraud

#routing for home page
@app.route('/')
def index():
    return render_template('index.html')

#routing to display results 
@app.route('/results', methods = ['Post'])
def results():
    #recieving data from frontend (file upload)
    data = request.files['transaction_data']

    #preprocessing the data 
    processed_data = load_data(data)
    #making fraud prediction
    prediction = predict_fraud(processed_data) 

    return render_template('results.html', prediction =prediction)
