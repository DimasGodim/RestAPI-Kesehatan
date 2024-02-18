from flask import Blueprint, jsonify, request
from database.model import planMenu, menuMakanan
from database.jalankan import create_engine_and_session

router = Blueprint('/admin', __name__, url_prefix='/admin')

@router.post('/make-plan-diet')
def makePlantDiet():
    meta = request.get_json()
    
    namaUser = meta.get('nama user', None)
    menuID = meta.get('menu-ID', [])
    jenisPlan = meta.get('jenis-plan') or 'menu-plan'
    targetKalori = meta.get('target-kalori')
    session = create_engine_and_session()
    
    response = {
        'menu': []
    }
    
    totalKalori = 0
    for menu in menuID:
        pilihanMenu = session.query(menuMakanan).filter_by(menuID=menu).first()
        
        pilihan = {
            'menu-ID': pilihanMenu.menuID,
            'nama-menu': pilihanMenu.namaMenu,
            'jumlah-satuan': f'{pilihanMenu.jumlah} {pilihanMenu.satuan}',
            'kalori/menu': pilihanMenu.jumlahKalori
        }
        
        response['menu'].append(pilihan)
        totalKalori += pilihanMenu.jumlahKalori

    save = planMenu(namaUser=namaUser, listMenu=response['menu'], totalKalori=totalKalori, jenisPlan=jenisPlan)
    save.planID = int(planMenu.generate_random_key())
    session.add(save)
    session.commit()

    response['menu'] = [{
        'menu-ID': item['menu-ID'],
        'nama-menu': item['nama-menu'],
        'jumlah-satuan': item['jumlah-satuan'],
        'kalori/menu': item['kalori/menu']
    } for item in response['menu']]

    response.update({
        'nama-user': namaUser,
        'plan-ID': save.planID,
        'jenis-plan': save.jenisPlan,
        'total-kalori': totalKalori
    })

    if targetKalori < totalKalori:
        response.update({
            'pesan-response': 'menu anda melebihi target kalori yang anda buat'
        })
    else:
        response.update({
            'pesan-response': 'Kesehatan adalah kekayaan sejati, bukan kepingan emas dan perak'
        })
    
    session.close()
    return jsonify([response])

@router.post('/granted-wish-menu')
def endpointGrantWishMenu():
    meta = request.get_json()

    wishMenuID = meta.get('wish-menu-ID')