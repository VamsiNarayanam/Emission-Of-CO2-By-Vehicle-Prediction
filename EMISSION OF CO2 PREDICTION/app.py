import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load('linear_regression_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])

def predict():
    '''
    For rendering results on HTML GUI
    '''

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    if output >= 400:
        return render_template('index.html',
                               prediction_text='CO2 EMISSION OF VEHICLE: {} G/KM IS EXTREMELY HIGH EMISSION'.format(
                                   output))

    elif output > 300:
        return render_template('index.html',
                               prediction_text='CO2 EMISSION OF VEHICLE: {} G/KM IS A VERY HIGH EMISSION'.format(
                                   output))

    elif output > 250:
        return render_template('index.html',
                               prediction_text='CO2 EMISSION OF VEHICLE: {} G/KM IS A HIGH EMISSION'.format(output))

    elif output > 200:
        return render_template('index.html',
                               prediction_text='CO2 EMISSION OF VEHICLE: {} G/KM IS A HIGHER EMISSION'.format(output))

    elif output > 150:
        return render_template('index.html',
                               prediction_text='CO2 EMISSION OF VEHICLE: {} G/KM IS A MODERATE EMISSION'.format(output))

    elif output > 100:
        return render_template('index.html',
                               prediction_text='CO2 EMISSION OF VEHICLE: {} G/KM IS A LOW EMISSION'.format(output))

    elif output >= 0:
        return render_template('index.html',
                               prediction_text='CO2 EMISSION OF VEHICLE: {} G/KM IS A VERY LOW EMISSION'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
