from fastapi import APIRouter

from app.api.v1.endpoints import ads, comments, login, privileges, users, categories

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(ads.router, prefix="/ads", tags=["ads"])
api_router.include_router(comments.router, prefix="/ads", tags=["comments"])
api_router.include_router(privileges.router, prefix="/privileges", tags=["privileges"])
