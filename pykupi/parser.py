from typing import Union

from .base import BaseClient
from .types import KupiSection, Discount
from .utils import get_page_url

MAX_PRICE = 99999999.0


class KupiParser(BaseClient):
    async def get_prices(
        self,
        item_id: str,
        min_price: Union[int, float] = 0.0,
        max_price: Union[int, float] = MAX_PRICE,
    ) -> Discount:
        page_url = get_page_url(KupiSection.DISCOUNT, item_id)
        results = await self.request(page_url)
        discount = Discount(**results)
        if max_price or min_price:
            discount.filter_offers_by_price(min_price, max_price)
        return discount
