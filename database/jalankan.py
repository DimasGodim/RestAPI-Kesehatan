from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs import config
def create_engine_and_session():
    engine = create_engine(config.url_database, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session