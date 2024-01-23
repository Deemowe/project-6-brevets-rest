from flask import Flask, jsonify, make_response, Response, request
from flask_restful import Resource, Api
from pymongo import MongoClient
from collections import OrderedDict
import arrow
import os
import json
import csv
from io import StringIO




app = Flask(__name__)
api = Api(app)
mongo_hostname = os.environ.get('hostname') # Get MongoDB hostname from environment variables

client = MongoClient(mongo_hostname, 27017) # Connect to the MongoDB instance
db = client.brevetdb # Connect to 'brevetdb' database


# class ListAll(Resource):
#     def get(self):
#         brevets_data = db.controls.find({})
#         formatted_brevets = []

#         for brevet in brevets_data:
#             formatted_controls = []
#             for control in brevet["controls"]:
#                 formatted_control = OrderedDict([
#                     ("km", control["km"]),
#                     ("mi", control["mi"]),
#                     ("location", control.get("location")),
#                     ("open", control["open"]),
#                     ("close", control["close"])
#                 ])
#                 formatted_controls.append(formatted_control)

#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", formatted_controls)
#             ])
#             formatted_brevets.append(formatted_brevet)

#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})




# class ListOpenOnly(Resource):
#     def get(self):
#         brevets_data = db.controls.find({})
#         formatted_brevets = []

#         for brevet in brevets_data:
#             formatted_controls = []
#             for control in brevet["controls"]:
#                 formatted_control = OrderedDict([
#                     ("km", control["km"]),
#                     ("mi", control["mi"]),
#                     ("location", control.get("location")),
#                     ("open", control["open"])
#                 ])
#                 formatted_controls.append(formatted_control)

#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", formatted_controls)
#             ])
#             formatted_brevets.append(formatted_brevet)

#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})


# class ListCloseOnly(Resource):
#     def get(self):
#         brevets_data = db.controls.find({})
#         formatted_brevets = []

#         for brevet in brevets_data:
#             formatted_controls = []
#             for control in brevet["controls"]:
#                 formatted_control = OrderedDict([
#                     ("km", control["km"]),
#                     ("mi", control["mi"]),
#                     ("location", control.get("location")),
#                     ("close", control["close"])
#                 ])
#                 formatted_controls.append(formatted_control)

#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", formatted_controls)
#             ])
#             formatted_brevets.append(formatted_brevet)

#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})





# api.add_resource(ListAll, '/listAll/')
# api.add_resource(ListOpenOnly, '/listOpenOnly/')
# api.add_resource(ListCloseOnly, '/listCloseOnly/')


# def format_brevets(brevets_data, top, open_only=False, close_only=False):
#     formatted_brevets = []
#     for brevet in brevets_data:
#         formatted_controls = []
#         for control in brevet["controls"]:
#             control_data = OrderedDict([
#                 ("km", control["km"]),
#                 ("mi", control["mi"]),
#                 ("location", control.get("location")),
#             ])
#             if open_only:
#                 control_data["open"] = control["open"]
#             elif close_only:
#                 control_data["close"] = control["close"]
#             else:
#                 control_data["open"] = control["open"]
#                 control_data["close"] = control["close"]
#             formatted_controls.append(control_data)

#         # Sort and limit the controls
#         key = 'open' if open_only else 'close' if close_only else None
#         if key:
#             formatted_controls = sorted(formatted_controls, key=lambda x: x[key])[:top]

#         formatted_brevet = OrderedDict([
#             ("distance", brevet["distance"]),
#             ("begin_date", brevet["begin_date"]),
#             ("begin_time", brevet["begin_time"]),
#             ("controls", formatted_controls)
#         ])
#         formatted_brevets.append(formatted_brevet)
#     return formatted_brevets




# class ListAll(Resource):
#     def get(self, format='json'):
#         top = request.args.get('top', default=None, type=int)
#         brevets_data = db.controls.find({})
#         formatted_brevets = self.format_brevets(brevets_data)

#         if format == 'csv':
#             return self.generate_csv_response(formatted_brevets)
#         else:  # default to JSON
#             return self.generate_json_response(formatted_brevets)

#     @staticmethod
#     def format_brevets(brevets_data):
#         formatted_brevets = []
#         for brevet in brevets_data:
#             formatted_controls = []
#             for control in brevet["controls"]:
#                 formatted_control = OrderedDict([
#                     ("km", control["km"]),
#                     ("mi", control["mi"]),
#                     ("location", control.get("location")),
#                     ("open", control["open"]),
#                     ("close", control["close"])
#                 ])
#                 formatted_controls.append(formatted_control)

#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", formatted_controls)
#             ])
#             formatted_brevets.append(formatted_brevet)
#         return formatted_brevets

#     @staticmethod
#     def generate_csv_response(formatted_brevets):
#         si = StringIO()
#         cw = csv.writer(si)

#         # Write CSV headers
#         # cw.writerow(["distance", "begin_date", "begin_time", "km", "mi", "location", "open", "close"])
#             # Write CSV headers
#         cw.writerow([
#             "brevets/distance", "brevets/begin_date", "brevets/begin_time", 
#             "brevets/controls/km", "brevets/controls/mi", 
#             "brevets/controls/location", "brevets/controls/open", "brevets/controls/close"
#         ])

#         # Write data rows
#         for brevet in formatted_brevets:
#             for control in brevet["controls"]:
#                 cw.writerow([brevet["distance"], brevet["begin_date"], brevet["begin_time"],
#                              control["km"], control["mi"], control["location"],
#                              control["open"], control["close"]])

#         output = make_response(si.getvalue())
#         output.headers["Content-Disposition"] = "attachment; filename=brevets.csv"
#         output.headers["Content-type"] = "text/csv"
#         return output
    

    

#     @staticmethod
#     def generate_json_response(formatted_brevets):
#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})





# class ListOpenOnly(Resource):
#     def get(self, format='json'):
#         top = request.args.get('top', default=None, type=int)
#         brevets_data = db.controls.find({})
#         formatted_brevets = self.format_brevets(brevets_data)

#         if format == 'csv':
#             return self.generate_csv_response(formatted_brevets)
#         else:  # default to JSON
#             return self.generate_json_response(formatted_brevets)

#     @staticmethod
#     def format_brevets(brevets_data):
#         formatted_brevets = []
#         for brevet in brevets_data:
#             formatted_controls = []
#             for control in brevet["controls"]:
#                 formatted_control = OrderedDict([
#                     ("km", control["km"]),
#                     ("mi", control["mi"]),
#                     ("location", control.get("location")),
#                     ("open", control["open"])
#                 ])
#                 formatted_controls.append(formatted_control)

#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", formatted_controls)
#             ])
#             formatted_brevets.append(formatted_brevet)
#         return formatted_brevets

#     @staticmethod
#     def generate_csv_response(formatted_brevets):
#         si = StringIO()
#         cw = csv.writer(si)

#         # Write CSV headers
#         # cw.writerow(["distance", "begin_date", "begin_time", "km", "mi", "location", "open"])
#         cw.writerow([
#             "brevets/distance", "brevets/begin_date", "brevets/begin_time", 
#             "brevets/controls/km", "brevets/controls/mi", 
#             "brevets/controls/location", "brevets/controls/open"
#         ])

#         # Write data rows
#         for brevet in formatted_brevets:
#             for control in brevet["controls"]:
#                 cw.writerow([brevet["distance"], brevet["begin_date"], brevet["begin_time"],
#                              control["km"], control["mi"], control["location"],
#                              control["open"]])

#         output = make_response(si.getvalue())
#         output.headers["Content-Disposition"] = "attachment; filename=open_times.csv"
#         output.headers["Content-type"] = "text/csv"
#         return output

#     @staticmethod
#     def generate_json_response(formatted_brevets):
#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})





# class ListCloseOnly(Resource):
#     def get(self, format='json'):
#         top = request.args.get('top', default=None, type=int)
#         brevets_data = db.controls.find({})
#         formatted_brevets = self.format_brevets(brevets_data)

#         if format == 'csv':
#             return self.generate_csv_response(formatted_brevets)
#         else:  # default to JSON
#             return self.generate_json_response(formatted_brevets)

#     @staticmethod
#     def format_brevets(brevets_data):
#         formatted_brevets = []
#         for brevet in brevets_data:
#             formatted_controls = []
#             for control in brevet["controls"]:
#                 formatted_control = OrderedDict([
#                     ("km", control["km"]),
#                     ("mi", control["mi"]),
#                     ("location", control.get("location")),
#                     ("close", control["close"])
#                 ])
#                 formatted_controls.append(formatted_control)

#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", formatted_controls)
#             ])
#             formatted_brevets.append(formatted_brevet)
#         return formatted_brevets

#     @staticmethod
#     def generate_csv_response(formatted_brevets):
#         si = StringIO()
#         cw = csv.writer(si)

#         # Write CSV headers
#         # cw.writerow(["distance", "begin_date", "begin_time", "km", "mi", "location", "close"])
#         cw.writerow([
#             "brevets/distance", "brevets/begin_date", "brevets/begin_time", 
#             "brevets/controls/km", "brevets/controls/mi", 
#             "brevets/controls/location","brevets/controls/close"
#         ])

#         # Write data rows
#         for brevet in formatted_brevets:
#             for control in brevet["controls"]:
#                 cw.writerow([brevet["distance"], brevet["begin_date"], brevet["begin_time"],
#                              control["km"], control["mi"], control["location"],
#                              control["close"]])

#         output = make_response(si.getvalue())
#         output.headers["Content-Disposition"] = "attachment; filename=close_times.csv"
#         output.headers["Content-type"] = "text/csv"
#         return output

#     @staticmethod
#     def generate_json_response(formatted_brevets):
#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})








# api.add_resource(ListAll, '/listAll/', '/listAll/<string:format>')
# api.add_resource(ListOpenOnly, '/listOpenOnly/', '/listOpenOnly/<string:format>')
# api.add_resource(ListCloseOnly, '/listCloseOnly/', '/listCloseOnly/<string:format>')





# def format_brevets(brevets_data, top, open_only=False, close_only=False):
#     formatted_brevets = []
#     for brevet in brevets_data:
#         formatted_controls = []
#         for control in brevet["controls"]:
#             control_data = OrderedDict([
#                 ("km", control["km"]),
#                 ("mi", control["mi"]),
#                 ("location", control.get("location")),
#             ])
#             if open_only:
#                 control_data["open"] = control["open"]
#             elif close_only:
#                 control_data["close"] = control["close"]
#             else:
#                 control_data["open"] = control["open"]
#                 control_data["close"] = control["close"]
#             formatted_controls.append(control_data)

#         # Sort and limit the controls
#         key = 'open' if open_only else 'close' if close_only else None
#         if key:
#             formatted_controls = sorted(formatted_controls, key=lambda x: x[key])[:top]

#         formatted_brevet = OrderedDict([
#             ("distance", brevet["distance"]),
#             ("begin_date", brevet["begin_date"]),
#             ("begin_time", brevet["begin_time"]),
#             ("controls", formatted_controls)
#         ])
#         formatted_brevets.append(formatted_brevet)
#     return formatted_brevets




# class ListAll(Resource):
#     # Handle GET request
#     def get(self, format='json'):
#         top = request.args.get('top', default=None, type=int)
#         brevets_data = db.controls.find({})
#         formatted_brevets = self.format_brevets(brevets_data, top)

#         # Return CSV or JSON based on the 'format' parameter
#         if format == 'csv':
#             return self.generate_csv_response(formatted_brevets)
#         else:  # default to JSON
#             return self.generate_json_response(formatted_brevets)

#     @staticmethod
#     def format_brevets(brevets_data, top=None):
#         formatted_brevets = []
#         for brevet in brevets_data:
#             formatted_controls = sorted(brevet["controls"], key=lambda x: x['open'])[:top] if top else brevet["controls"]
#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", formatted_controls)
#             ])
#             formatted_brevets.append(formatted_brevet)
#         return formatted_brevets

#     @staticmethod
#     def generate_csv_response(formatted_brevets):
#         si = StringIO()
#         cw = csv.writer(si)

#         # Write CSV headers
#         # cw.writerow(["distance", "begin_date", "begin_time", "km", "mi", "location", "open", "close"])
#             # Write CSV headers
#         cw.writerow([
#             "brevets/distance", "brevets/begin_date", "brevets/begin_time", 
#             "brevets/controls/km", "brevets/controls/mi", 
#             "brevets/controls/location", "brevets/controls/open", "brevets/controls/close"
#         ])

#         # Write data rows
#         for brevet in formatted_brevets:
#             for control in brevet["controls"]:
#                 cw.writerow([brevet["distance"], brevet["begin_date"], brevet["begin_time"],
#                              control["km"], control["mi"], control["location"],
#                              control["open"], control["close"]])

#         output = make_response(si.getvalue())
#         output.headers["Content-Disposition"] = "attachment; filename=brevets.csv"
#         output.headers["Content-type"] = "text/csv"
#         return output
    

    

#     @staticmethod
#     def generate_json_response(formatted_brevets):
#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})





# class ListOpenOnly(Resource):
#     def get(self, format='json'):
#         top = request.args.get('top', default=None, type=int)
#         brevets_data = db.controls.find({})
#         formatted_brevets = self.format_brevets(brevets_data, top, open_only=True)

#         if format == 'csv':
#             return self.generate_csv_response(formatted_brevets)
#         else:  # default to JSON
#             return self.generate_json_response(formatted_brevets)

#     @staticmethod
#     def format_brevets(brevets_data, top=None, open_only=False):
#         formatted_brevets = []
#         for brevet in brevets_data:
#             formatted_controls = sorted(brevet["controls"], key=lambda x: x['open'])[:top] if top else brevet["controls"]
#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", [OrderedDict([
#                     ("km", control["km"]),
#                     ("mi", control["mi"]),
#                     ("location", control.get("location")),
#                     ("open", control["open"])]) for control in formatted_controls if open_only])
#             ])
#             formatted_brevets.append(formatted_brevet)
#         return formatted_brevets

#     @staticmethod
#     def generate_csv_response(formatted_brevets):
#         si = StringIO()
#         cw = csv.writer(si)

#         # Write CSV headers
#         # cw.writerow(["distance", "begin_date", "begin_time", "km", "mi", "location", "open"])
#         cw.writerow([
#             "brevets/distance", "brevets/begin_date", "brevets/begin_time", 
#             "brevets/controls/km", "brevets/controls/mi", 
#             "brevets/controls/location", "brevets/controls/open"
#         ])

#         # Write data rows
#         for brevet in formatted_brevets:
#             for control in brevet["controls"]:
#                 cw.writerow([brevet["distance"], brevet["begin_date"], brevet["begin_time"],
#                              control["km"], control["mi"], control["location"],
#                              control["open"]])

#         output = make_response(si.getvalue())
#         output.headers["Content-Disposition"] = "attachment; filename=open_times.csv"
#         output.headers["Content-type"] = "text/csv"
#         return output

#     @staticmethod
#     def generate_json_response(formatted_brevets):
#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})





# class ListCloseOnly(Resource):
#     def get(self, format='json'):
#         top = request.args.get('top', default=None, type=int)
#         brevets_data = db.controls.find({})
#         formatted_brevets = self.format_brevets(brevets_data, top, close_only=True)

#         if format == 'csv':
#             return self.generate_csv_response(formatted_brevets)
#         else:  # default to JSON
#             return self.generate_json_response(formatted_brevets)

#     @staticmethod
#     def format_brevets(brevets_data, top=None, close_only=False):
#         formatted_brevets = []
#         for brevet in brevets_data:
#             if close_only:
#                 formatted_controls = sorted(brevet["controls"], key=lambda x: x['close'])[:top] if top else brevet["controls"]
#             else:
#                 formatted_controls = brevet["controls"]

#             formatted_brevet = OrderedDict([
#                 ("distance", brevet["distance"]),
#                 ("begin_date", brevet["begin_date"]),
#                 ("begin_time", brevet["begin_time"]),
#                 ("controls", [OrderedDict([
#                     ("km", control["km"]),
#                     ("mi", control["mi"]),
#                     ("location", control.get("location")),
#                     ("close", control["close"])]) for control in formatted_controls if close_only])
#             ])
#             formatted_brevets.append(formatted_brevet)
#         return formatted_brevets

#     @staticmethod
#     def generate_csv_response(formatted_brevets):
#         si = StringIO()
#         cw = csv.writer(si)

#         # Write CSV headers
#         # cw.writerow(["distance", "begin_date", "begin_time", "km", "mi", "location", "close"])
#         cw.writerow([
#             "brevets/distance", "brevets/begin_date", "brevets/begin_time", 
#             "brevets/controls/km", "brevets/controls/mi", 
#             "brevets/controls/location","brevets/controls/close"
#         ])

#         # Write data rows
#         for brevet in formatted_brevets:
#             for control in brevet["controls"]:
#                 cw.writerow([brevet["distance"], brevet["begin_date"], brevet["begin_time"],
#                              control["km"], control["mi"], control["location"],
#                              control["close"]])

#         output = make_response(si.getvalue())
#         output.headers["Content-Disposition"] = "attachment; filename=close_times.csv"
#         output.headers["Content-type"] = "text/csv"
#         return output

#     @staticmethod
#     def generate_json_response(formatted_brevets):
#         response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
#         return make_response(response_json, 200, {'Content-Type': 'application/json'})




# api.add_resource(ListAll, '/listAll/', '/listAll/<string:format>')
# api.add_resource(ListOpenOnly, '/listOpenOnly/', '/listOpenOnly/<string:format>')
# api.add_resource(ListCloseOnly, '/listCloseOnly/', '/listCloseOnly/<string:format>')






# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')





class BrevetResource(Resource):
    # @staticmethod
    # def generate_csv_response(formatted_brevets, include_open=True, include_close=True):
    #     si = StringIO()
    #     cw = csv.writer(si)
    #     headers = [
    #         "brevets/distance", "brevets/begin_date", "brevets/begin_time", 
    #         "brevets/controls/km", "brevets/controls/mi", "brevets/controls/location"
    #     ]
    #     if include_open:
    #         headers.append("brevets/controls/open")
    #     if include_close:
    #         headers.append("brevets/controls/close")
    #     cw.writerow(headers)

    #     for brevet in formatted_brevets:
    #         for control in brevet["controls"]:
    #             row = [brevet["distance"], brevet["begin_date"], brevet["begin_time"],
    #                    control["km"], control["mi"], control["location"]]
    #             if include_open:
    #                 row.append(control.get("open"))
    #             if include_close:
    #                 row.append(control.get("close"))
    #             cw.writerow(row)

    #     output = make_response(si.getvalue())
    #     # filename = "brevets.csv" if include_open and include_close else "open_times.csv" if include_open else "close_times.csv"
    #     # output.headers["Content-Disposition"] = f"attachment; filename={filename}"
    #     output.headers["Content-type"] = "text/plain"
    #     return output
    @staticmethod
    def generate_csv_response(formatted_brevets, include_open=True, include_close=True):
        si = StringIO()
        cw = csv.writer(si)

        # Define the headers
        headers = ["brevets/distance", "brevets/begin_date", "brevets/begin_time"]
        max_controls = max(len(brevet["controls"]) for brevet in formatted_brevets)
        for i in range(max_controls):
            headers.extend([
                f"brevets/controls/{i}/km",
                f"brevets/controls/{i}/mi",
                f"brevets/controls/{i}/location"
            ])
            if include_open:
                headers.append(f"brevets/controls/{i}/open")
            if include_close:
                headers.append(f"brevets/controls/{i}/close")
        
        cw.writerow(headers)

        # Write data for each brevet
        for brevet in formatted_brevets:
            row = [brevet["distance"], brevet["begin_date"], brevet["begin_time"]]
            for i in range(max_controls):
                control = brevet["controls"][i] if i < len(brevet["controls"]) else {"km": "", "mi": "", "location": "", "open": "", "close": ""}
                row.extend([control["km"], control["mi"], control["location"]])
                if include_open:
                    row.append(control.get("open", ""))
                if include_close:
                    row.append(control.get("close", ""))
            cw.writerow(row)

        output = make_response(si.getvalue())
        output.headers["Content-type"] = "text/plain"
        return output

    @staticmethod
    def generate_json_response(formatted_brevets):
        response_json = json.dumps({"brevets": formatted_brevets}, indent=4)
        return make_response(response_json, 200, {'Content-Type': 'application/json'})

    @staticmethod
    def format_brevets(brevets_data, top=None, open_only=False, close_only=False):
        formatted_brevets = []
        for brevet in brevets_data:
            formatted_controls = []
            for control in brevet["controls"]:
                control_data = OrderedDict([
                    ("km", control["km"]),
                    ("mi", control["mi"]),
                    ("location", control.get("location")),
                ])
                if open_only or not close_only:
                    control_data["open"] = control.get("open")
                if close_only or not open_only:
                    control_data["close"] = control.get("close")
                formatted_controls.append(control_data)

            # Apply sorting and limiting only if 'top' parameter is provided
            if top is not None:
                key = 'open' if open_only else 'close' if close_only else None
                if key:
                    formatted_controls = sorted(formatted_controls, key=lambda x: x[key])[:top]

            formatted_brevet = OrderedDict([
                ("distance", brevet["distance"]),
                ("begin_date", brevet["begin_date"]),
                ("begin_time", brevet["begin_time"]),
                ("controls", formatted_controls)
            ])
            formatted_brevets.append(formatted_brevet)
        return formatted_brevets

class ListAll(BrevetResource):
    def get(self, format='json'):
        brevets_data = db.controls.find({})  # Replace with your MongoDB query
        formatted_brevets = self.format_brevets(brevets_data)

        if format == 'csv':
            return self.generate_csv_response(formatted_brevets)
        else:
            return self.generate_json_response(formatted_brevets)

class ListOpenOnly(BrevetResource):
    def get(self, format='json'):
        top = request.args.get('top', default=None, type=int)
        brevets_data = db.controls.find({})  # Replace with your MongoDB query
        formatted_brevets = self.format_brevets(brevets_data, top, open_only=True)

        if format == 'csv':
            return self.generate_csv_response(formatted_brevets, include_close=False)
        else:
            return self.generate_json_response(formatted_brevets)

class ListCloseOnly(BrevetResource):
    def get(self, format='json'):
        top = request.args.get('top', default=None, type=int)
        brevets_data = db.controls.find({})  # Replace with your MongoDB query
        formatted_brevets = self.format_brevets(brevets_data, top, close_only=True)

        if format == 'csv':
            return self.generate_csv_response(formatted_brevets, include_open=False)
        else:
            return self.generate_json_response(formatted_brevets)

api.add_resource(ListAll, '/listAll/', '/listAll/<string:format>')
api.add_resource(ListOpenOnly, '/listOpenOnly/', '/listOpenOnly/<string:format>')
api.add_resource(ListCloseOnly, '/listCloseOnly/', '/listCloseOnly/<string:format>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




