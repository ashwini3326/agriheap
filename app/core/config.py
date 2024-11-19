from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Define your configuration settings here
    app_name: str = "Agriheap"
    app_version: str = "0.1"
    api_v1_str: str = "/v1"
    environment: str = "development"  # Default to 'development'
    database_url: str = "sqlite:///./test.db"  # Default to SQLite for development
    secret_key: str = "mysecretkey"  # Just an example, should be changed in production


    class Config:
        # You can set additional config options here like case sensitivity or env file location
        env_file = ".env"  # Load environment variables from the .env file
        env_file_encoding = "utf-8"

# Instantiate the settings class
settings = Settings()