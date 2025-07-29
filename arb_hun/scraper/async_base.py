import random, httpx, asyncio
from bs4 import BeautifulSoup
from arb_hun.config import settings
from arb_hun.logger import log
from arb_hun.proxies import proxy_manager
from typing import Optional

class AsyncScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def fetch(self, path: str) -> Optional[BeautifulSoup]:
        url = f"{self.base_url}{path}"
        for attempt in range(1, settings.depth + 1):
            try:
                proxies = proxy_manager.get()
                async with httpx.AsyncClient(proxies=proxies, timeout=settings.timeout) as c:
                    r = await c.get(url); r.raise_for_status()
                    return BeautifulSoup(r.text, "html.parser")
            except Exception as e:
                backoff = 2**attempt + random.random()
                log.warning("fetch_retry", url=url, attempt=attempt, error=str(e))
                await asyncio.sleep(backoff)
        log.error("fetch_fail", url=url)
        return None
