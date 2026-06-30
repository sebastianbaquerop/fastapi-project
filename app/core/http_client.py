from typing import Protocol, runtime_checkable
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential,retry_if_exception_type

class HTTPClient:

    def __init__(self):
        self.client = httpx.AsyncClient(timeout=httpx.Timeout(5.0))
    
    async def close(self):
        await self.client.aclose()
    
    @retry(
            stop=stop_after_attempt(3), 
            wait=wait_exponential(multiplier=1, min=2, max=5), 
            retry=retry_if_exception_type((httpx.ConnectTimeout, httpx.RemoteProtocolError, httpx.HTTPStatusError)))
    async def request(self, method: str, url: str, **kwargs):
        response = await self.client.request(method=method,url=url, **kwargs)
        response.raise_for_status()
        return response.json()

    async def get(self, url: str, **kwargs):
        return await self.request(method="GET",url=url, **kwargs)

