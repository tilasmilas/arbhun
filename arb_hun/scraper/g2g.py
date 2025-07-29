from typing import List, Dict
from arb_hun.scraper.async_base import AsyncScraper

class G2GScraper(AsyncScraper):
    async def search(self, keyword: str) -> List[Dict]:
        soup = await self.fetch(f"/search?query={keyword}")
        items: List[Dict] = []
        if soup:
            for card in soup.select(".product-item"):
                title = card.select_one(".title").get_text(strip=True)
                price = float(card.select_one(".price").get_text(strip=True).replace("$",""))
                url = card.select_one("a")["href"]
                items.append({"title": title, "price": price, "url": url, "source": "g2g"})
        return items
