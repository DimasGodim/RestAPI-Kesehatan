from flask import Blueprint, request, jsonify
from database.jalankan import create_engine_and_session
from database.model import menuMakanan, planMenu, wishlistMenu

router = Blueprint('/user', __name__, url_prefix='/user')

@router.get('/list-menu')
def listMenu():
    session = create_engine_and_session()

    all_menus = session.query(menuMakanan).all()

    response = []

    for menu in all_menus:
        data = {
            'menu-ID': menu.menuID,
            'nama-menu': menu.namaMenu,
            'jumlah-satuan': f'{menu.jumlah} {menu.satuan}',
            'kalori': menu.jumlahKalori
        }

        response.append(data)
    
    session.close()

    return jsonify(response)

@router.get('/see-plan-diet')
def seePlanDiet():
    planmenuID = int(request.args.get('plan-menu-ID'))
    session = create_engine_and_session()
    data = session.query(planMenu).filter_by(planID=planmenuID).first()
    return jsonify(
        {
            'plan-ID': data.planID,
            'jenis-plan': data.jenisPlan,
            'nama-user': f'{data.namaUser}',
            'menu': data.listMenu,
            'total-kalori': data.totalKalori 
        }
    )

@router.post('/make-plan-diet')
def makePlantDiet():
    meta = request.get_json()
    
    namaUser = meta.get('nama user', None)
    menuID = meta.get('menu-ID', [])
    targetKalori = meta.get('target-kalori')
    session = create_engine_and_session()
    
    response = {
        'menu': []
    }
    
    totalKalori = 0
    for menu in menuID:
        pilihanMenu = session.query(menuMakanan).filter_by(menuID=menu).first()
        
        if pilihanMenu is None:
            return jsonify(
                {
                    'eror-message': 'cannot find your chossen menu'
                }
            ),404
        
        pilihan = {
            'menu-ID': pilihanMenu.menuID,
            'nama-menu': pilihanMenu.namaMenu,
            'jumlah-satuan': f'{pilihanMenu.jumlah} {pilihanMenu.satuan}',
            'kalori/menu': pilihanMenu.jumlahKalori
        }
        
        response['menu'].append(pilihan)
        totalKalori += pilihanMenu.jumlahKalori

    save = planMenu(namaUser=namaUser, listMenu=response['menu'], totalKalori=totalKalori, jenisPlan='diet-plan')
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
        'total-kalori': totalKalori,
        'jenis-plan': 'plan-diet'
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

@router.post('/wish-menu')
def wishMenu():
    meta = request.get_json()
    
    namaMenu = meta.get('nama-menu')
    jumlah = meta.get('jumlah')
    satuan = meta.get('satuan')
    kalori = meta.get('kalori')
    deskripsi = meta.get('deskripsi-menu', None)
    
    save = wishlistMenu(namaMenu=namaMenu, jumlah=jumlah, satuan=satuan, kalori=kalori, deskripsiMenu=deskripsi)
    save.wishID = wishlistMenu.generate_random_key()
    session = create_engine_and_session()
    session.add(save)
    session.commit()
    meta['status'] = 'permohonan menu anda telah berhasil dimasukan dalam antrian wish menu'
    meta['wish-ID'] = save.wishID
    return jsonify(meta)