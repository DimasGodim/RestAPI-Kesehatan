from typing import Optional

def HitungBMI(berat: float, tinggi: float, gender: bool): # kebutuhan tubuh dalam kondisi paling minimal
    
    if gender == True: # laki laki
        nilai_BMI = berat / (tinggi ** 2)
        print(nilai_BMI)
    elif gender == False: # perempuan
        nilai_BMI = berat / (tinggi ** 2) * 1.1 
        print(nilai_BMI)
    
    # OUTPUT
    if nilai_BMI < 18.5:
        return {
            'nilai-BMI': nilai_BMI,
            'klasifikasi-berat': 'kurus',
            'kalimat-saran': 'Anda mungkin perlu mempertimbangkan peningkatan asupan kalori untuk mencapai berat badan yang sehat',
            'saran-menu': 'Pilih makanan tinggi protein seperti telur dan kacang-kacangan, serta nikmati buah-buahan seperti pisang untuk tambahan kalori'
        }
    elif 18.5 <= nilai_BMI < 24.9:
        return {
            'nilai-BMI': nilai_BMI,
            'klasifikasi-berat': 'normal',
            'kalimat-saran': 'Berat badan Anda berada dalam kisaran sehat. Pertahankan pola makan seimbang dan gaya hidup aktif',
            'saran-menu': 'Pertahankan pola makan seimbang dengan sayuran berwarna-warni, protein seperti ayam, dan karbohidrat kompleks seperti nasi merah. Sertakan buah-buahan seperti apel atau jeruk'
        }
    elif 25 <= nilai_BMI < 29.9:
        return {
            'nilai-BMI': nilai_BMI,
            'klasifikasi-berat': 'gemuk',
            'kalimat-saran': 'Pertahankan pola makan sehat dan pertimbangkan peningkatan aktivitas fisik untuk mencapai berat badan yang lebih sehat',
            'saran-menu': 'Pilih protein rendah lemak seperti ikan atau tahu, kombinasikan dengan karbohidrat kompleks seperti kentang atau beras merah. Sertakan buah-buahan segar seperti anggur atau mangga'
        }
    elif 30 <= nilai_BMI < 34.9:
        return {
            'nilai-BMI': nilai_BMI,
            'klasifikasi-berat': "Obesitas Kelas 1",
            'kalimat-saran': 'Penting untuk memulai perubahan pola makan dan aktivitas fisik yang lebih sehat. Konsultasikan dengan profesional kesehatan',
            'saran-menu': 'Fokus pada serat tinggi dengan sayuran seperti brokoli, protein rendah lemak seperti daging tanpa lemak, dan buah-buahan segar seperti jeruk atau apel'
        }
    elif 35 <= nilai_BMI < 39.9:
        return {
            'nilai-BMI': nilai_BMI,
            'klasifikasi-berat': "Obesitas Kelas 2",
            'kalimat-saran': 'Segera konsultasikan dengan profesional kesehatan untuk perencanaan penurunan berat badan yang aman dan efektif',
            'saran-menu': 'Makanan tinggi protein seperti daging, telur, dan kacang-kacangan dan biji-bijian untuk menambahkan asupan kalori serta buah-buahan yang kaya nutrisi'
        }
    else:
        return {
            'nilai-BMI': nilai_BMI,
            'klasifikasi-berat': "Obesitas Kelas 3",
            'kalimat-saran': 'Segera konsultasikan dengan profesional kesehatan untuk perencanaan penurunan berat badan yang aman dan efektif',
            'saran-menu': 'Mulailah dengan perubahan kecil, pilih sayuran hijau, protein berkualitas seperti ayam tanpa kulit, dan variasi buah-buahan seperti buah delima atau buah naga'
        }

def HitungBMR (gender: bool, berat_badan: float , tinggi_badan: float , usia: int): # # kebutuhan kalori tubuh dalam kondisi paling minimal
    if gender == 1: # pria
        nilai_BMR = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan) - (5.677 * usia)
    elif gender == 0: # wanita
        nilai_BMR = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan) - (4.330 * usia)
    else:
        return False    
    if nilai_BMR < 1200:
        return {
            'nilai-BMR': nilai_BMR,
            'klasifikasi-BMR': 'sangat rendah',
            'kalimat-saran': 'sangat penting untuk berkonsultasi dengan profesional kesehatan atau ahli gizi untuk mendapatkan panduan yang tepat. Fokus pada makanan bergizi tinggi untuk memenuhi kebutuhan nutrisi tanpa mengorbankan kesehatan',
            'plan-diet': 'sangat penting untuk melakukan diet di bawah pengawasan profesional kesehatan. Fokus pada makanan bergizi tinggi dan pertimbangkan untuk memasukkan nutrisi tambahan agar kebutuhan tubuh terpenuhi'
        }
    elif 1200 <= nilai_BMR <= 1500:
        return {
            'nilai-BMR': nilai_BMR,
            'klasifikasi-BMR': 'rendah',
            'kalimat-saran': 'disarankan untuk memilih makanan yang kaya nutrisi seperti sayuran hijau, protein tanpa lemak, dan buah-buahan. Penting untuk memastikan kecukupan nutrisi meskipun dalam batasan kalori yang lebih rendah',
            'plan-diet': 'Anda masih dapat merencanakan diet dengan memilih makanan yang kaya nutrisi. Prioritaskan asupan protein, sayuran, dan buah-buahan, dan pertimbangkan untuk merencanakan makanan sepanjang hari untuk menjaga energi dan keseimbangan nutrisi'
        }
    elif 1500 <= nilai_BMR <= 1800:
        return {
            'nilai-BMR': nilai_BMR,
            'klasifikasi-BMR': 'sedang',
            'kalimat-saran': 'pertahankan keseimbangan asupan protein, karbohidrat, dan lemak. Pilih sumber nutrisi yang seimbang dan pertimbangkan untuk memasukkan variasi makanan agar asupan nutrisi tetap optimal',
            'plan-diet': 'Anda memiliki fleksibilitas yang lebih besar dalam merencanakan diet. Pastikan untuk menjaga keseimbangan antara protein, karbohidrat, dan lemak. Sertakan makanan beragam untuk memastikan kebutuhan nutrisi terpenuhi'
        }
    elif nilai_BMR > 1800:
        return {
            'nilai-BMR': nilai_BMR,
            'klasifikasi-BMR': 'tinggi',
            'kalimat-saran': 'fokuslah pada memenuhi kebutuhan kalori yang lebih besar dengan sumber protein berkualitas tinggi, lemak sehat, dan karbohidrat kompleks. Diversifikasi makanan untuk memastikan asupan nutrisi yang cukup',
            'plan-diet': 'Anda dapat merencanakan diet yang mendukung aktivitas fisik dan kebutuhan kalori yang lebih besar. Pilih sumber protein berkualitas tinggi, lemak sehat, dan karbohidrat kompleks. Jangan lupa untuk tetap memerhatikan asupan nutrisi secara menyeluruh'
        }
    
def HitungTDEE(BMR: float, rating_aktivitas: int): # kebutuhan kalori yang dibutuhkan oleh tubuh berdasarkan kegiatan
    
    NilaiTDEE = BMR * (1 + rating_aktivitas / 10)

    return NilaiTDEE

def MakePlanDiet(berat_badan: Optional[float] = None, tinggi_badan: Optional[float] = None, usia: Optional[int] = None, gender: Optional[bool] = None, rate_aktivitas: Optional[float] = None, nilaiBMR: Optional[float] = None, nilaiTDEE: Optional[float] = None): # menciptakan planing kalori yang dibutuhkan untuk diet
    
    if nilaiTDEE is None:
        if nilaiBMR is None:
            NilaiBMR = HitungBMR(gender=gender, berat_badan=berat_badan, tinggi_badan=tinggi_badan, usia=usia)
        NilaiBMR = nilaiBMR
        NilaiTDEE = HitungTDEE(BMR=NilaiBMR, rating_aktivitas=rate_aktivitas)
    
    NilaiTDEE = nilaiTDEE

    KaloriDiet = NilaiTDEE - 300

    return KaloriDiet