from flask import Flask, jsonify, request
from kalkulator import HitungBMI, HitungBMR, HitungTDEE

app = Flask(__name__)

@app.get('/get-BMI')
def test():
    tinggiBadan = request.args.get('tinggi')
    beratBadan = request.args.get('berat')

    NilaiBMI = HitungBMI(berat=beratBadan, tinggi=tinggiBadan)