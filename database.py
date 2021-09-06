from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user_name_db = 'surglin'
password_db = 'Nusha230399'
db_name = 'alchemy_core_db'


SQLACHEMY_DATABASE_URL = f"postgresql://{user_name_db}:{password_db}@localhost/{db_name}"


engine = create_engine(SQLACHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()