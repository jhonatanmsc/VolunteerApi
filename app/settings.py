from decouple import config as env
import logging
import os

log = logging.getLogger()
log.setLevel(logging.DEBUG)


class PostgresConfiguration:
    POSTGRES_DB_PORT = env('POSTGRES_PORT', default='5433')
    POSTGRES_DB_NAME = env('POSTGRES_DB', default='volunteer')
    POSTGRES_DB_LOGIN = env('POSTGRES_USER', default='volunteer')
    POSTGRES_DB_PASSWORD = env('POSTGRES_PASSWORD', default='volunteer')
    POSTGRES_DB_ADDRESS = env('POSTGRES_ADDRESS', default='localhost')

    @property
    def postgres_db_path(self):
        return f'postgres://{self.POSTGRES_DB_LOGIN}:{self.POSTGRES_DB_PASSWORD}@' \
                f'{self.POSTGRES_DB_ADDRESS}:' \
                f'{self.POSTGRES_DB_PORT}/{self.POSTGRES_DB_NAME}'
