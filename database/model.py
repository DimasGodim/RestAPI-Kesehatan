from sqlalchemy import Column, Integer, String, Text, Float, JSON, func
from sqlalchemy.ext.declarative import declarative_base
from database.jalankan import Create_Engine
import random
import string

Base = declarative_base()
engine = Create_Engine()

class menuMakanan(Base):
    __tablename__ = 'MenuMakanan'
    menuID = Column(Integer, primary_key=True, server_default=func.floor(func.rand() * 1000000))
    namaMenu = Column(String(225))
    jumlah = Column(Float)
    satuan = Column(String(225))
    jumlahKalori = Column(Float)

    @staticmethod
    def generate_random_key():
        return ''.join(random.choices(string.digits, k=6))

class planMenu(Base):
    __tablename__ = 'PlanMakanan'
    planID = Column(Integer, primary_key=True, server_default=func.floor(func.rand() * 1000000))
    namaUser = Column(String(225), nullable = True)
    listMenu = Column(JSON)
    totalKalori = Column(Float)

    @staticmethod
    def generate_random_key():
        return ''.join(random.choices(string.digits, k=6))

class dataUser(Base):
    __tablename__ = 'DataUser'
    userId = Column(Integer, primary_key=True, server_default=func.floor(func.rand() * 1000000))
    nama = Column(String(225), nullable = True)
    tinggiBadan = Column(Float, nullable = True)
    beratBadan = Column(Float, nullable = True)
    BMI = Column(Float, nullable = True)
    BMR = Column(Float, nullable = True)
    TDEE = Column(Float, nullable = True)

    @staticmethod
    def generate_random_key():
        return ''.join(random.choices(string.digits, k=6))

class wishlistMenu(Base):
    __tablename__ = 'WishlistMenu'
    wishID = Column(Integer, primary_key=True, server_default=func.floor(func.rand() * 1000000))
    namaMenu = Column(String(225))
    berat = Column(Float)
    satuan = Column(String(225))
    kalori = Column(Float)
    deskripsiMenu = Column(Text, nullable = True)

    @staticmethod
    def generate_random_key():
        return ''.join(random.choices(string.digits, k=6))
    
Base.metadata.create_all(engine)