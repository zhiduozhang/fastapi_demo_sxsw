from fastapi.routing import APIRouter

from demo.web.api import monitoring

api_router = APIRouter()
api_router.include_router(views.router, prefix="/monitoring")
