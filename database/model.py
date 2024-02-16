from sqlalchemy import Column, Integer, String, Sequence, Float, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class menuMakanan(Base):
    __tablename__ = 'MenuMakanan'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    makananPokok = Column(JSON, nullable = True)
    snack = Column(JSON, nullable = True)

class dataUser(Base):
    __tablename__ = 'DataUser'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nama = Column(String, nullable = True)
    tinggiBadan = Column(Float, nullable = True)
    beratBadan = Column(Float, nullable = True)
    BMI = Column(Float, nullable = True)
    BMR = Column(Float, nullable = True)
    TDEE = Column(Float, nullable = True)

class wishlistMenu(Base):
    __tablename__ = 'WishlistMenu'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    jenisMakanan = Column(String)
    beratMakanan = Column(Float)
    kaloriMakanan = Column(Float)

class saranMakanan(Base):
    __tablename__ = 'SaranMakanan'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    namaClient = Column(String)
    menuYangDisarankan = Column(JSON)