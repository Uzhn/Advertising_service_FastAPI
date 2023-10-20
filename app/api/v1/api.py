from fastapi import APIRouter

from app.api.v1.endpoints import users, login, ads, privileges

api_router = APIRouter()

api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(ads.router, prefix="/ads", tags=["ads"])
api_router.include_router(privileges.router, prefix="/privileges", tags=["privileges"])
