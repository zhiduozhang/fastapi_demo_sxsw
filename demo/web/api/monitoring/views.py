from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """
    try:
        return {"status": "OK"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API is not healthy",
        ) from None
