from datetime import date
from typing import List, Union, Optional
from pydantic import BaseModel, Field, field_validator


__all__ = ["Offer", "Discount"]

class Offer(BaseModel):
    offered_by: str = Field(alias="offeredBy")
    price: float
    price_currency: str = Field(alias="priceCurrency")
    valid_until: date = Field(alias="priceValidUntil")
    amount: Optional[str] = Field(default="various amounts")


class Discount(BaseModel):
    name: str
    brand: str = Field(default="Unknown Brand")
    image: str
    description: str
    offers: List[Offer] = Field(default=[])

    @field_validator("offers", mode="before")
    def extract_offers(cls, v):
        return [Offer(**offer_data) for offer_data in v.get("offers")]

    @property
    def low_price(self) -> float:
        if not self.offers:
            return 0.0
        return min([offer.price for offer in self.offers])

    @property
    def high_price(self) -> float:
        if not self.offers:
            return 0.0
        return max([offer.price for offer in self.offers])

    def filter_offers_by_price(
        self, min_price: Union[int, float], max_price: Union[int, float]
    ):
        self.offers = list(
            filter(lambda offer: min_price <= offer.price <= max_price, self.offers)
        )


class KupiSection(str):
    DISCOUNT = "sleva"
