from flask import Blueprint, request
from database.jalankan import create_engine_and_session
from database.model import menuMakanan

router = Blueprint(url_prefix='/user')

@router.get('/list-menu')
async def listMenu():
    menuMakanan

@router.post('/make-plant-diet')
async def makePlantDiet():
    meta = request.get_json()
    
    namaUser = meta.get('namaUser', None)
    makananPokok = meta.get()
    sessionDatabase = create_engine_and_session()
    