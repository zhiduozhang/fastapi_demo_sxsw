from fastapi import APIRouter
from fastapi.responses import HTTPResponse

router = APIRouter()


@router.get("/health")
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """

@router.get("/hello")
def hello_world() -> HTTPResponse:
    return HTTPResponse(content="hello world!", status_code=200)
