from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_engine_and_session(database_url):
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session