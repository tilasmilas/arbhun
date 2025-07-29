from typing import List, Dict
from arb_hun.scraper.async_base import AsyncScraper

class Z2UScraper(AsyncScraper):
    async def search(self, keyword: str) -> List[Dict]:
        soup = await self.fetch(f"/listings?search={keyword}")
        items: List[Dict] = []
        if soup:
            for card in soup.select(".listing"):
                title = card.select_one("h3").get_text(strip=True)
                price = float(card.select_one(".cost").get_text(strip=True).replace("USD",""))
                url = card.select_one("a")["href"]
                items.append({"title": title, "price": price, "url": url, "source": "z2u"})
        return items
