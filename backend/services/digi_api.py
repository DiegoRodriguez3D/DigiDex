"""Service layer for consuming the external Digi-API."""

import httpx
from typing import Any

DIGI_API_BASE = "https://digi-api.com/api/v1"


class DigiAPIClient:
    """Async client for the Digi-API."""

    def __init__(self):
        self.base_url = DIGI_API_BASE
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(timeout=30.0)
        return self._client

    async def close(self):
        if self._client:
            await self._client.aclose()
            self._client = None

    async def get_digimon_list(self, page: int = 0, page_size: int = 20) -> dict[str, Any]:
        """Fetch paginated list of Digimon."""
        client = await self._get_client()
        response = await client.get(
            f"{self.base_url}/digimon",
            params={"page": page, "pageSize": page_size}
        )
        response.raise_for_status()
        return response.json()

    async def get_digimon_detail(self, id_or_name: str | int) -> dict[str, Any]:
        """Fetch detailed info for a single Digimon."""
        client = await self._get_client()
        response = await client.get(f"{self.base_url}/digimon/{id_or_name}")
        response.raise_for_status()
        return response.json()

    async def search_digimon(self, name: str) -> dict[str, Any]:
        """Search Digimon by name."""
        client = await self._get_client()
        response = await client.get(
            f"{self.base_url}/digimon",
            params={"name": name}
        )
        response.raise_for_status()
        return response.json()


# Singleton instance
digi_api_client = DigiAPIClient()
