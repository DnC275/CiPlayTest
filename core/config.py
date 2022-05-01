from pydantic import BaseSettings


class DBSettings(BaseSettings):
    username: str
    password: str
    db: str
    host: str
    port: str

    class Config:
        env_prefix = "POSTGRES_"
        env_file = ".env"