from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB: str = "sqlite:///test.db"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


config = Settings()
