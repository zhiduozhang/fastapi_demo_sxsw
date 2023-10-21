from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> None:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """

@router.get("/hello")
def hello_world() -> str:
    """
    Returns a greeting.

    It returns 'hello world!'.
    """
    return 'hello world!'
