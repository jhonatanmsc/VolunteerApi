from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from decouple import config as env

DATABASES = {
    'default': 'postgres://{}:{}@{}:{}/{}'.format(
        env("POSTGRES_USER"),
        env("POSTGRES_PASSWORD"),
        env("POSTGRES_ADDRESS"),
        env("POSTGRES_PORT"),
        env("POSTGRES_NAME")
    )
}

engine = create_engine(DATABASES['default'])
meta = MetaData(engine)
Base = declarative_base()
