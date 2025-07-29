import itertools, asyncio, httpx
from arb_hun.config import settings
from arb_hun.logger import log

class ProxyManager:
    def __init__(self):
        self._all = settings.proxies
        self._alive = []

    async def health_check(self):
        async def check(p):
            try:
                async with httpx.AsyncClient(proxies={"http":p,"https":p}, timeout=5) as c:
                    r = await c.get("https://httpbin.org/ip")
                    if r.status_code == 200: return p
            except:
                log.warning("proxy_fail", proxy=p)
            return None
        res = await asyncio.gather(*(check(p) for p in self._all))
        self._alive = [p for p in res if p]
        if not self._alive:
            log.error("no healthy proxies"); exit(1)
        log.info("proxies_alive", count=len(self._alive))
        self._pool = itertools.cycle(self._alive)

    def get(self):
        return {"http": next(self._pool), "https": next(self._pool)}

proxy_manager = ProxyManager()
