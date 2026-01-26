from datetime import date
from typing import List, Union, Optional
from pydantic import BaseModel, Field, field_validator


__all__ = ["Offer", "Discount"]

class Offer(BaseModel):
    offered_by: str = Field(alias="offeredBy")
    price: float
    price_currency: str = Field(alias="priceCurrency")
    amount: Optional[str] = Field(default=" ")


class Discount(BaseModel):
    name: str
    brand: str = Field(default="Unknown")
    image: str 
    description: str = ""
    offers: List[Offer] = Field(default=[])

    @field_validator("offers", mode="before")
    def extract_offers(cls, v):
        return [Offer(**offer_data) for offer_data in v.get("offers")]



