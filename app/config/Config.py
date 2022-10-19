from os import environ
from dataclasses import dataclass


@dataclass
class Config:
    """
    Configuration
    """
    APP_NAME: str = "Oauth"
    APP_VERSION: float = 1.0
    DB_VERSION: float = 1.0

    BASE_API_TIME: float = 0.5

    NAVER_CLIENT_ID: str = "Hroaj_C3BtBESULJGyEH"
    NAVER_SECRET_KEY: str = "m392nslok3"
    NAVER_REDIRECT_URI: str = "http://localhost:8000/naverLogin"
    NAVER_STATE: str = "RANDOM STATE"

@dataclass
class LocalConfig(Config):
    """
    Local(Testing) Configuration
    """
    RELOAD: bool = True
    PORT: int = 8000
    LOGGING: bool = False


@dataclass
class ProductionConfig(Config):
    """
    Production Configuration
    """
    RELOAD: bool = False
    PORT: int = 80
    LOGGING: bool = True


configs = {
    "production": ProductionConfig(),
    "local": LocalConfig()
}
config = configs[environ.get((Config.APP_NAME + "_CONFIG"), "local")]