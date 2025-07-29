from typing import Dict
from arb_hun.logger import log
from arb_hun.config import settings

async def purchase_item(item: Dict) -> bool:
    if not settings.auto_purchase:
        return False
    log.info("purchase_stub", item=item)
    return True
