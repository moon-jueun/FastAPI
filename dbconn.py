from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DBconn:
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 5432
        self.USER_NAME = 'jueun'
        self.PASSWORD = 'answndms9812*'
        self.DBNAME = 'je_test'

    def get_db_engine(self):
        '''
        Function Description
        1) serssionmaker():
            actual database session
        2) declarative_base():
            create each of the database models or classes (the ORM models)
        '''

        url = f'postgresql://{self.user_name}:{self.password}@localhost:{self.port}/{self.dbname}'
        engine = create_engine(url, convert_unicode=False, encoding='utf-8')
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()

        return engine
