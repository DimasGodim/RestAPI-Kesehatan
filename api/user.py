from flask import Blueprint, request, jsonify
from database.jalankan import create_engine_and_session
from database.model import menuMakanan, planMenu

router = Blueprint(url_prefix='/user')

@router.get('/list-menu')
def listMenu():
    session = create_engine_and_session()

    all_menus = session.query(menuMakanan).all()

    response = []

    for menu in all_menus:
        data = {
            'menu ID': menu.menuID,
            'nama': menu.namaMenu,
            'jumlah satuan': f'{menu.jumlah} {menu.satuan}', 
            'jumlah kalori': f'{menu.jumlahKalori}'
        }
        response.append(data)
    
    session.close()

    return jsonify(response)

@router.get('/see-plan-diet')
def seePlanDiet():
    planmenuID = request.args.get('plan-menu-ID')
    session = create_engine_and_session()

@router.post('/make-plant-diet')
def makePlantDiet():
    meta = request.get_json()
    
    namaUser = meta.get('nama user', None)
    menuID = meta.get('menu-ID', [])
    targetKalori = meta.get('target-kalori')
    session = create_engine_and_session()
    
    response = []
    
    totalKalori: float = 0
    for menu in menuID:
        pilihanMenu = session.query(menuMakanan).filter_by(menuID=menu).first()
        
        pilihan = {
            'nama-menu': pilihanMenu.namaMenu,
            'jumlah-satuan': f'{pilihanMenu.jumlah} {pilihanMenu.satuan}',
            'kalori/menu': pilihanMenu.jumlahKalori
        }
        
        response.append(pilihan)
        totalKalori += pilihanMenu.jumlahKalori

    save = planMenu(namaUser = namaUser, listMenu = response, listMenu = response, totalKalori = totalKalori)
    session.add(save)
    session.commit
    session.close()

    response.append(
        {
            'nama-user': namaUser
        }
    )

    response.append({
        'total-kalori': totalKalori
    })
    
    if targetKalori < totalKalori:
        response.append(
            {
                'pesan-response': 'menu anda melebihi target kalori yang anda buat'
            }
        )
    else:
        response.append(
            {
                'pesan-response': 'Kesehatan adalah kekayaan sejati, bukan kepingan emas dan perak'
            }
        )
    
    return jsonify(response)