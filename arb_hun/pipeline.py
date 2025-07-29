import asyncio
from typing import List, Dict
from arb_hun.scraper.g2g import G2GScraper
from arb_hun.scraper.z2u import Z2UScraper
from arb_hun.matcher import match_items
from arb_hun.profit import calculate_profit
from arb_hun.alerts import notify
from arb_hun.purchase import purchase_item
from arb_hun.proxies import proxy_manager
from arb_hun.config import settings

async def run_pipeline(
    keyword: str,
    min_roi: float = None,
    alert: bool = False,
    auto: bool = False
) -> List[Dict]:
    await proxy_manager.health_check()
    a, b = await asyncio.gather(
        G2GScraper(settings.g2g_url).search(keyword),
        Z2UScraper(settings.z2u_url).search(keyword)
    )
    matches = match_items(a, b)
    results = []
    threshold = min_roi if min_roi is not None else settings.roi_threshold
    for buy, sell, score in matches:
        stats = calculate_profit(buy, sell)
        if stats["margin"] >= threshold:
            item = {**buy, **sell, **stats, "score": score}
            if auto:
                await purchase_item(item)
            results.append(item)
    if alert:
        notify(results)
    return results
