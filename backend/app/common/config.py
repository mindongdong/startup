from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator

class Settings(BaseSettings):
    ROUTES_STR: str = "/routes"
    SERVER_NAME: str = None
    SERVER_HOST: AnyHttpUrl = None

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "test"
    SENTRY_DSN: Optional[HttpUrl] = None
    
settings = Settings()