from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    gemini_api_key: str = ""
    gemini_model: str = "gemini-3.8-flash"

    backend_url: str = "http://127.0.0.1:8000"
    host: str = "127.0.0.1"
    port: int = 8000

    app_name: str = "LegalEase"
    company_name: str = "LegalEase"
    company_tagline: str = "AI-Powered Legal Document Generator"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()