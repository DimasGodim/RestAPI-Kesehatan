from flask import Blueprint, request, jsonify, session
from helper.kalkulator import HitungBMI, HitungBMR, HitungTDEE, MakePlanDiet

routes = Blueprint(url_prefix='/Kalkulator')

@routes.get('/BMI')
def endpointBMI():
    berat = request.args.get('berat-badan')
    tinggi = request.args.get('tinggi-badan')
    gender = request.args.get('gender')
    userId = request.args.get('user-ID', default=None)

    NilaiBMI = HitungBMI(berat=berat, tinggi=tinggi, gender=gender)

    return jsonify(NilaiBMI)

@routes.get('/BMR')
def endpointBMR():
    berat = request.args.get('berat-badan')
    tinggi = request.args.get('tinggi-badan')
    usia = request.args.get('usia')
    gender = request.args.get('gender')
    userId = request.args.get('user-ID', default=None)

    NilaiBMR = HitungBMR(gender=gender, berat_badan=berat, tinggi_badan=tinggi, usia=usia)

    session['BMR'] = request.form[NilaiBMR['nilai bmr']]

    return jsonify (NilaiBMR)

@routes.get('/TDEE')
def endpointTDEE():
    berat = request.args.get('berat-badan')
    tinggi = request.args.get('tinggi-badan')
    usia = request.args.get('usia')
    gender = request.args.get('gender')
    rateAktivitas = request.args.get('rate-aktivitas')
    userId = request.args.get('user-ID', default=None)

    NilaiBMR = session.get('BMR')
    if NilaiBMR is None:
        NilaiBMR = HitungBMR(gender=gender, berat_badan=berat, tinggi_badan=tinggi, usia=usia)
    
    NilaiBMI = HitungBMI(berat=berat, tinggi=tinggi, gender=gender)
    NilaiTDEE = HitungTDEE(BMR=NilaiBMR, rating_aktivitas=rateAktivitas)
    KaloriDiet = MakePlanDiet(nilaiTDEE=NilaiTDEE)

    return jsonify(
        {
            'nilai BMR': NilaiBMR,
            'nilai TDEE': NilaiTDEE,
            'nilai BMI': NilaiBMI['nilai BMI'],
            'klasifikasi berat': NilaiBMI['klasifikasi berat'],
            'kalori yang disarankan untuk diet ringan': KaloriDiet
        }
    )