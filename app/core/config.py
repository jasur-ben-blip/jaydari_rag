from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
    )

    app_name: str = 'jaydari_rag'
    log_level: str = 'INFO'

    qdrant_url: str 
    qdrant_api_key: str
    qdrant_collection: str
    qdrant_timeout: float = 10.0

    embedding_model: str

    llm_model: str
    llm_adapter_path: str | None = None
    llm_device: str = 'cpu'
    llm_max_new_tokens: int = 256
    llm_temperature: float = 0.2
    
    rag_enabled: bool = True
    rag_mode: str = 'auto'
    top_k: int = 5
    max_context_chars: int = 4000
    min_score: float = 0.25
    min_score_strict: float = 0.35
    max_sources: int = 2
    chunk_size_chars: int = 1200
    chunk_overlap_chars: int = 200
    qdrant_timeout: float = 10.0


settings = Settings()
