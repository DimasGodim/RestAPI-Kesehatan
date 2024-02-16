from sqlalchemy import Column, Integer, String, Sequence, Float, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class menuMakanan(Base):
    __tablename__ = 'MenuMakanan'
    menuID = Column(Integer, Sequence('menuID_seq'), primary_key=True)
    namaUser = Column(String, nullable= True)
    makananPokok = Column(JSON, nullable = True)
    makananRingan = Column(JSON, nullable = True)
    minuman = Column(JSON, nullable = True)
    jumlahCalori = Column(Integer, nullable = True)

class dataUser(Base):
    __tablename__ = 'DataUser'
    userId = Column(Integer, Sequence('userID_seq'), primary_key=True)
    nama = Column(String, nullable = True)
    tinggiBadan = Column(Float, nullable = True)
    beratBadan = Column(Float, nullable = True)
    BMI = Column(Float, nullable = True)
    BMR = Column(Float, nullable = True)
    TDEE = Column(Float, nullable = True)

class wishlistMenu(Base):
    __tablename__ = 'WishlistMenu'
    wishID = Column(Integer, Sequence('wishID_seq'), primary_key=True)
    jenisMakanan = Column(String)
    beratMakanan = Column(Float)
    kaloriMakanan = Column(Float)