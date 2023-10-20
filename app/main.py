import uvicorn
from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app import initial_data

app = FastAPI(title='Advertising service')

app.include_router(api_router, prefix=settings.API_V1_STR)
initial_data.init()

# if __name__ == "__main__":
#     initial_data.init()
#     uvicorn.run(app, host="0.0.0.0", port=8000)

