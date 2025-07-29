from typing import Dict
from arb_hun.config import settings

def calculate_profit(buy: Dict, sell: Dict) -> Dict:
    buy_cost = buy["price"] * (1 + settings.platform_fee + settings.payment_fee)
    sell_net = sell["price"] * (1 - settings.platform_fee - settings.payment_fee)
    profit = sell_net - buy_cost
    margin = profit / buy_cost if buy_cost else 0.0
    return {"profit": profit, "margin": margin}
