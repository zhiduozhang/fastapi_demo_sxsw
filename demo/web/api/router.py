from fastapi.routing import APIRouter

def hello_world():
    return "Hello, World!"

from demo.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.get("/hello", response_model=str)(hello_world)
