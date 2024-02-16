from flask import Blueprint, request, jsonify
from helper.kalkulator import HitungBMI, HitungBMR, HitungTDEE
routes = Blueprint(url_prefix='/Kalkulator')

@routes.get('/bmi')
def endpointBMI():
    berat = request.args.get('beratBadan')
    tinggi = request.args.get('tinggiBadan')
    gender = request.args.get('gender')

    NilaiBMI = HitungBMI(berat=berat, tinggi=tinggi, gender=gender)

    return jsonify(NilaiBMI)

@routes.get('/bmr')
def endpointBMR():
    berat = request.args.get('beratBadan')
    tinggi = request.args.get('tinggiBadan')
    usia = request.args.get('usia')
    gender = request.args.get('gender')

    NilaiBMR = HitungBMR(gender=gender, berat_badan=berat, tinggi_badan=tinggi, usia=usia)

    