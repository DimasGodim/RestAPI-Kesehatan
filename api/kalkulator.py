from flask import Blueprint, request, jsonify, session
from helper.kalkulator import HitungBMI, HitungBMR, HitungTDEE, MakePlanDiet

routes = Blueprint('/kalkulator', __name__, url_prefix='/kalkulator')

@routes.get('/BMI')
def endpointBMI():
    berat = float(request.args.get('berat-badan'))
    tinggi = float(request.args.get('tinggi-badan'))
    gender = bool(request.args.get('gender'))
    userId = request.args.get('user-ID', default=None)

    NilaiBMI = HitungBMI(berat=berat, tinggi=tinggi, gender=gender)

    return jsonify(NilaiBMI)

@routes.get('/BMR')
def endpointBMR():
    berat = float(request.args.get('berat-badan'))
    tinggi = float(request.args.get('tinggi-badan'))
    usia = int(request.args.get('usia'))
    gender = bool(request.args.get('gender'))
    userId = request.args.get('user-ID', default=None)

    NilaiBMR = HitungBMR(gender=gender, berat_badan=berat, tinggi_badan=tinggi, usia=usia)

    return jsonify (NilaiBMR)

@routes.get('/TDEE')
def endpointTDEE():
    berat = float(request.args.get('berat-badan'))
    tinggi = float(request.args.get('tinggi-badan'))
    usia = int(request.args.get('usia'))
    gender = bool(request.args.get('gender'))
    rateAktivitas = float(request.args.get('rate-aktivitas'))
    userId = request.args.get('user-ID', default=None)

    NilaiBMR = HitungBMR(gender=gender, berat_badan=berat, tinggi_badan=tinggi, usia=usia)
    
    NilaiBMI = HitungBMI(berat=berat, tinggi=tinggi, gender=gender)
    NilaiTDEE = HitungTDEE(BMR=NilaiBMR['nilai-BMR'], rating_aktivitas=rateAktivitas)
    KaloriDiet = MakePlanDiet(nilaiTDEE=NilaiTDEE)

    return jsonify(
        {
            'nilai BMR': NilaiBMR['nilai-BMR'],
            'nilai TDEE': NilaiTDEE,
            'nilai BMI': NilaiBMI['nilai-BMI'],
            'klasifikasi berat': NilaiBMI['klasifikasi-berat'],
            'kalori yang disarankan untuk diet ringan': KaloriDiet
        }
    )