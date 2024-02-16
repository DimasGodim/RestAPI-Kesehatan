def HitungBMI (berat: str, tinggi: float, gender: str): # Indeks Massa Tubuh
    
    nilai_bmi = berat / (tinggi ** 2)
    if nilai_bmi < 18.5:
        return {
            'nilai BMI': nilai_bmi,
            'klasifikasi_berat': 'kurus'
        }
    elif 18.5 <= nilai_bmi < 24.9:
        return {
            'nilai_BMI': nilai_bmi,
            'klasifikasi_berat': 'normal'
        }
    elif 25 <= nilai_bmi < 29.9:
        return {
            'nilai BMI': nilai_bmi,
            'klasifikasi_berat': 'gemuk'
        }
    elif 30<= nilai_bmi < 34.9:
        return {
            'nilai BMI': nilai_bmi,
            'klasifikasi_berat': "Obesitas Kelas 1"
        }
    elif 35 <= nilai_bmi < 39.9:
        return {
            'nilai BMI': nilai_bmi,
            'klasifikasi_berat': "Obesitas Kelas 2"
        }
    else:
        return {
            'nilai BMI': nilai_bmi,
            'klasifikasi_berat': "Obesitas Kelas 3"
        }

def HitungBMR (gender: str, berat_badan: float , tinggi_badan: float , usia: int): # jumlah kalori yang digunakan oleh tubuh posisi standby
    
    if gender == 'pria':
        nilai_bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan) - (5.677 * usia)
    elif gender == 'wanita':
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan) - (4.330 * usia)
    else:
        return False
    
    return {
        'nilai_bmr': nilai_bmr
    }

def HitungTDEE(BMR: float, rating_aktivitas: int):
    
    NilaiTdee = BMR * (1 + rating_aktivitas / 10)
    
    return NilaiTdee