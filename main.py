from fastapi import FastAPI

from app import initial_data
from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(title="Advertising service")

app.include_router(api_router, prefix=settings.API_V1_STR)
initial_data.main()
