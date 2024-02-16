from sqlalchemy import Column, Integer, String, Sequence, Float, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class menuMakanan(Base):
    __tablename__ = 'MenuMakanan'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    makananPokok = Colomn(JSON, nullable = True)
    snack = Colomn(JSON, nullable = True)

class dataUser(Base):
    __tablename__ = 'DataUser'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nama = Colomn(String, nullable = True)
    tinggiBadan = Column(Float, nullable = True)
    beratBadan = Column(Float, nullable = True)
    BMI = Column(Float, nullable = True)
    BMR = Column(Float, nullable = True)
    TDEE = Column(Float, nullable = True)