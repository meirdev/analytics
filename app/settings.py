import pathlib

from pydantic import BaseSettings, PostgresDsn

BASE_DIR = pathlib.Path(__file__).parent.parent


class Settings(BaseSettings):
    pg_dsn: PostgresDsn
    ip2location_bin: pathlib.Path = BASE_DIR / "data" / "IP2LOCATION-LITE-DB11.BIN"
    static_dir: pathlib.Path = BASE_DIR / "static"


settings = Settings()
