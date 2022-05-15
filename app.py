from flask import Flask, request, jsonify
import os
import numpy as np
from prediction_service import prediction

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def welcome():
    return "Welcome to Home Page"

@app.route("/predict", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            if request.json:
                response = prediction.api_response(request.json)
                return jsonify(response)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)