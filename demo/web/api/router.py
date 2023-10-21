from fastapi.routing import APIRouter

from demo.web.api import monitoring
from demo.web.api.endpoints import reset_password

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(reset_password.router, prefix="/reset-password")
