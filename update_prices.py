import asyncio
from parser import KupiParser
from models import session, Store, Drink


def clear(drink: Drink):
    drink.discount = False
    drink.discount_cost = 0

async def update_all():
    parser = KupiParser()
    drinks = session.query(Drink).all()
    stores = session.query(Store).all()
    stores_table = {store.name: store for store in stores}

    try: 
        for drink in drinks: 
            try:
                raw = await parser.get_prices(drink.name)
                filtered_offers = []
                for offer in raw.offers:
                    # check both object and json attribute to make pydantic quiet
                    store_name = offer.offered_by if isinstance(offer.offered_by, str) else getattr(offer.offered_by, 'name', str(offer.offered_by))
                    if store_name.lower() in stores_table:
                        filtered_offers.append(offer)

                if filtered_offers:
                    lowest_cost = getattr(filtered_offers[0], 'price', getattr(filtered_offers[0], 'cost', 0))
                    if lowest_cost:
                        drink.discount = True
                        drink.discount_cost = lowest_cost
                        drink.offered_amount = getattr(filtered_offers[0], 'amount', '')
                        
                        if isinstance(filtered_offers[0]. offered_by, str):
                            store_name = filtered_offers[0].offered_by
                        else:
                            store_name = getattr(filtered_offers[0].offered_by, 'name', str(filtered_offers[0]. offered_by))
                        drink.store = stores_table[store_name.lower()]
                    else: clear(drink)
                else: clear(drink)
                    
            except Exception as e:
                print(f"problem parsing drink {drink.name}: {e}")
                clear(drink)
                continue
                
        session.commit()
    finally:
        await parser.session.close()
        

if __name__ == "__main__":
    asyncio.run(update_all())