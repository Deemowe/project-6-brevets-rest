"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import logging

import arrow  # Replacement for datetime, based on moment.js
import flask
from flask import Flask, render_template, jsonify, request, redirect, url_for
import arrow
import acp_times  # brevet time calculations
from pymongo import MongoClient
import config


app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

# DB Section
client = MongoClient(host=CONFIG.HOSTNAME, port=27017)
db = client.brevetdb

@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('brevets.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from km, using rules
    described at https://rusa.org/pages/acp-brevet-control-times-calculator.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)

    brevet_distance_km = request.args.get('brevet_dist', 200, type=int)
    start_time_str = request.args.get('begin_time', arrow.now().isoformat(), type=str)
    start_date_str = request.args.get('begin_date', arrow.now().isoformat(), type=str)


    app.logger.debug(f"request.args: {request.args}")
    app.logger.debug(f"km={km}")

    # FIXME: These probably aren't the right open and close times and brevets may be longer than 200km
    #   they need more arguments from the front-end.
    # change 200 and arrow.now
    # open_time = acp_times.open_time(km, 200, arrow.now().isoformat)
    # close_time = acp_times.close_time(km, 200, arrow.now().isoformat)
    # result = {"open": open_time, "close": close_time}
    # return flask.jsonify(result=result)

    open_time_result = acp_times.open_time(km, brevet_distance_km, f"{start_date_str} {start_time_str}")
    close_time_result = acp_times.close_time(km, brevet_distance_km, f"{start_date_str} {start_time_str}")


    result = {"open": open_time_result, "close": close_time_result}
    return flask.jsonify(result=result)

# @app.route("/submit_controls", methods=["POST"])
# def submit_controls():
#     """
#     Accepts control times and inserts them into the database.
#     """
#     data = request.get_json()
#     controls = data['controls']
#     db.controls.insert_many(controls)  
#     return jsonify(success=True), 200

@app.route("/submit_controls", methods=["POST"])
def submit_controls():
    """
    Accepts control times and inserts them into the database.
    Only inserts controls with non-empty values.
    """
    db.controls.delete_many({})  # Clears the existing controls before inserting new ones

    data = request.get_json()
    controls = data['controls']
    distance = data.get('distance')
    begin_date = data.get('begin_date')
    begin_time = data.get('begin_time')

    # Store the distance, begin_date, and begin_time in each control
    for control in controls:
        control['distance'] = distance
        control['begin_date'] = begin_date
        control['begin_time'] = begin_time

    # Filter out controls that have all empty values for 'km', 'open_time', and 'close_time'
    valid_controls = [control for control in controls if control.get('km') or control.get('open_time') or control.get('close_time')]

    if valid_controls:  # Check if there are any valid controls to insert
        db.controls.insert_many(valid_controls)  # Insert the filtered controls
        return jsonify(success=True), 200
    else:
        return jsonify(success=False, error="Please enter at least one control time."), 400


@app.route("/display_controls")
def display_controls():
    """
    Fetches and displays control times from the database.
    """
    controls = list(db.controls.find())  # Retrieves all documents in the 'controls' collection
    return render_template('display_controls.html', controls=controls)



app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.logger.info(f"Opening for global access on port {CONFIG.PORT}")
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=True)
