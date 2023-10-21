from typing import Any, AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
@pytest.mark.asyncio
async def test_hello_world(client: AsyncClient):
    """
    Test function for the hello world endpoint.

    :param client: the test client.
    """
    response = await client.get("/api/monitoring/hello")
    if response.status_code != 200:
        raise Exception(f"Expected status code 200, but got {response.status_code}")
    if response.text != "hello world!":
        raise Exception(f"Expected content 'hello world!', but got {response.text}")

from demo.web.application import get_app


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """
    Backend for anyio pytest plugin.

    :return: backend name.
    """
    return "asyncio"


@pytest.fixture
def fastapi_app() -> FastAPI:
    """
    Fixture for creating FastAPI app.

    :return: fastapi app with mocked dependencies.
    """
    application = get_app()
    return application  # noqa: WPS331


@pytest.fixture
async def client(
    fastapi_app: FastAPI,
    anyio_backend: Any,
) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture that creates client for requesting server.

    :param fastapi_app: the application.
    :yield: client for the app.
    """
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac
