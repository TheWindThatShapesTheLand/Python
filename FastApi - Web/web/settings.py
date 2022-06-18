from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port:  int = 5346
    database_url = 'sqlite:////Users/Коптутер/PycharmProjects/Helpme/scr/web/database.sqlite3'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
