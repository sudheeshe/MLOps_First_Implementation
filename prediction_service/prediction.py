import yaml
import os
import json
import joblib
import numpy as np
from src.get_data import read_params
params_path = 'params.yaml'
schema_path = os.path.join('prediction_service', 'schema_in.json')

class NotInRange(Exception):
    def __init__(self, message ='Values entered are not in expected range'):
        self.message = message
        super().__init__((self.message))

class NotInCols(Exception):
    def __init__(self, message = "Not In cols"):
        self.message = message
        super().__init__(self.message)


def predict(data):
    config = read_params(params_path)
    model_dir_path = config['model_dir']
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]

    try:
        if 3 <= prediction <= 8:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected result"


def get_schema(schema_file_path = schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
        return schema


def validate_input(dict_request):
    def _validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotInCols

    def _validate_values(col, val):
        schema = get_schema()

        if not (schema[col]["min"] <= float(dict_request[col]) <= schema[col]["max"]):
            raise NotInRange

    for col, val in dict_request.items():
        _validate_cols(col)
        _validate_values(col, val)

    return True


def api_response(dict_request):

    try:
        if validate_input(dict_request):
            data = np.array([list(dict_request.values())])
            response = predict(data)
            response = {"response": response}
            return response

    except NotInRange as e:
        response = {"the_exected_range": get_schema(), "response": str(e)}
        return response

    except NotInCols as e:
        response = {"the_exected_cols": get_schema().keys(), "response": str(e)}
        return response


    except Exception as e:
        response = {"response": str(e)}
        return response

