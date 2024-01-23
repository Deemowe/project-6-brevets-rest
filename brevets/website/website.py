"""
Flask backend for user requests page
"""
import flask
from flask import Flask, render_template, request
import requests
import logging
import json
import os

###
# Globals
###
app = Flask(__name__)

# Environment vars for REST API
BACKEND_ADDR = os.environ['BACKEND_ADDR']
BACKEND_PORT = os.environ['BACKEND_PORT']

# Don't need any PyMongo / MongoDB code in here because that's handled in the REST API container

@app.route('/')
@app.route('/index')
def home():
    app.logger.debug("Main page entry")
    return render_template('index.html')

@app.route('/listAll')
def listeverything():
    csv = request.args.get('csv', type=str)

    # r = requests.get('http://restapi:5000/listAll')
    # Make a request to the REST API for the specified types of entries and in given format
    all_req = None
    if csv == "true":
        app.logger.debug("Sending a CSV request to the REST API")
        all_req = requests.get(f"http://{BACKEND_ADDR}:{BACKEND_PORT}/listAll/csv")
    else:
        app.logger.debug("Sending a JSON request to the REST API")
        all_req = requests.get(f"http://{BACKEND_ADDR}:{BACKEND_PORT}/listAll/json")

    all_text = all_req.text

    # This text is what will be sent to the client in requests.html
    return flask.jsonify( {"all_list" : all_text} )

# Route for listening opening times
@app.route('/listOpen')
def list_open_times():
    # Retrieve the values passed into the JSON request in requests.html
    csv = request.args.get('csv', type=str)
    top = request.args.get('top', type=int)

    # req = requests.get('http://restapi:5000/listOpen')
    # Make a request to the REST API for the specified types of entries and in given format
    open_req = None
    if csv == "true":
        open_req = requests.get(f"http://{BACKEND_ADDR}:{BACKEND_PORT}/listOpenOnly/csv?top={top}")
    else:
        open_req = requests.get(f"http://{BACKEND_ADDR}:{BACKEND_PORT}/listOpenOnly/json?top={top}")
    open_text = open_req.text

    # This text is what will be sent to the client in requests.html
    return flask.jsonify({"open_list" : open_text})


# Route for listing closing times
@app.route('/listClose')
def list_close_times():
    # Retrieve the values passed into the JSON request in requests.html
    csv = request.args.get('csv', type=str)
    top = request.args.get('top', type=int)

    # req = requests.get('http://restapi:5000/listClose')
    # Make a request to the REST API for the specified types of entries and in given format
    close_req = None
    if csv == "true":
        close_req = requests.get(f"http://{BACKEND_ADDR}:{BACKEND_PORT}/listCloseOnly/csv?top={top}")
    else:
        close_req = requests.get(f"http://{BACKEND_ADDR}:{BACKEND_PORT}/listCloseOnly/json?top={top}")
    close_text = close_req.text

    # This text is what will be sent to the client in requests.html
    return flask.jsonify({"close_list" : close_text})


#############
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)