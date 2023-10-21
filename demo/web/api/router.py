from fastapi.routing import APIRouter

from demo.web.api.monitoring import views

api_router = APIRouter()
api_router.include_router(views.router, prefix="/monitoring")
