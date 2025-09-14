from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB: str = "sqlite:///test.db"
    demo: bool = True # Init DB with demo data

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


config = Settings()
