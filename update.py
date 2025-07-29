import asyncio
from parser import KupiParser
from models import session, Drink, Store


async def update_prices():
    parser = KupiParser()
    drinks = session.query(Drink).all()
    stores = session.query(Store).all()
    stores_table = {store.name: store for store in stores}

    try:
        for drink in drinks:
            raw = await parser.get_prices(drink.name) 

            filtered_offers = [offer for offer in raw.offers if offer.offered_by.lower() in stores_table]

            if filtered_offers:
                lowest_cost = filtered_offers[0].price
                if lowest_cost < drink.normal_cost: 
                    drink.discount = True 
                    drink.discount_cost = lowest_cost
                    drink.offered_amount = filtered_offers[0].amount
                    display_store_name = filtered_offers[0].offered_by.lower()
                    drink.store = stores_table[display_store_name]
                else:
                    drink.discount = False
                    drink.discount_cost = 0
        session.commit()
    finally:
        await parser.session.close() # type: ignore
        

if __name__ == "__main__":
    asyncio.run(update_prices())