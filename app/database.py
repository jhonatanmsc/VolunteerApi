from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from .settings import PostgresConfiguration

pg = PostgresConfiguration()
engine = create_engine(pg.postgres_db_path)
meta = MetaData(engine)
Base = declarative_base()
