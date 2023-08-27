from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configurations.envs.envs import database

engine = create_engine(f"postgresql://{database['db_user']}:{database['db_password']}@{database['db_host']}:{database['db_port']}/{database['db_name']}")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
