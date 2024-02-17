from sqlalchemy import Column, Integer, String, Sequence, Float, JSON, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class menuMakanan(Base):
    __tablename__ = 'MenuMakanan'
    menuID = Column(Integer, Sequence('menuID_seq'), primary_key=True, server_default=func.floor(func.rand() * 1000000))
    namaMenu = Column(String(225))
    jumlah = Column(Float)
    satuan = Column(String(225))
    jumlahKalori = Column(Float)

class planMenu(Base):
    __tablename__ = 'MenuMakanan'
    menuID = Column(Integer, Sequence('menuID_seq'), primary_key=True, server_default=func.floor(func.rand() * 1000000))
    namaUser = Column(String(225), nullable = True)
    listMenu = Column(JSON)
    totalKalori = Column(Float)

class dataUser(Base):
    __tablename__ = 'DataUser'
    userId = Column(Integer, Sequence('userID_seq'), primary_key=True, server_default=func.floor(func.rand() * 1000000))
    nama = Column(String(225), nullable = True)
    tinggiBadan = Column(Float, nullable = True)
    beratBadan = Column(Float, nullable = True)
    BMI = Column(Float, nullable = True)
    BMR = Column(Float, nullable = True)
    TDEE = Column(Float, nullable = True)

class wishlistMenu(Base):
    __tablename__ = 'WishlistMenu'
    wishID = Column(Integer, Sequence('wishID_seq'), primary_key=True, server_default=func.floor(func.rand() * 1000000))
    jenisMakanan = Column(String(225))
    beratMakanan = Column(Float)
    kaloriMakanan = Column(Float)