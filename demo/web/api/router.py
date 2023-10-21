from fastapi.routing import APIRouter

from demo.web.api import monitoring
from demo.web.api.monitoring.views import hello_world

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.add_api_route("/hello", hello_world, response_model=str)
