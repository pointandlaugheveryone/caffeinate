from config import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Store, Drink
import os


engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

albert = Store(name='albert', display_name='Albert', logo_url='images/albert.svg')
billa = Store(name='billa', display_name='BILLA', logo_url='images/billa.svg')
globus = Store(name='globus', display_name='Globus', logo_url='images/globus.svg')
kaufland = Store(name='kaufland', display_name='Kaufland', logo_url='images/kaufland.svg')
lidl = Store(name='lidl', display_name='Lidl', logo_url='images/lidl.svg')
norma = Store(name='norma', display_name='NORMA', logo_url='images/norma.svg')
penny = Store(name='penny',display_name='Penny', logo_url='images/penny.svg')
tesco = Store(name='tesco', display_name='Tesco', logo_url='images/tesco.svg')
session.add_all([albert, billa, globus, kaufland, lidl, norma, penny, tesco])

cola = Drink(name='limonada-coca-cola', display_name='Coca-Cola', normal_cost=50.4, discount_cost=0, image_url='images/drinks/cola.jpg', is_zero=False)
cola_zero = Drink(name='limonada-coca-cola-zero', display_name='Coca-Cola-Zero', normal_cost=50.4, discount_cost=0, image_url='images/drinks/cola_zero.jpg', is_zero=True)
pepsi = Drink(name='limonada-pepsi', display_name='Pepsi', normal_cost=46.3, discount_cost=0, image_url='images/drinks/pepsi.jpg', is_zero=False)
pepsi_max = Drink(name='limonada-bez-kalorii-max-pepsi', display_name='Pepsi Max', normal_cost=46.3, discount_cost=0, image_url='images/drinks/pepsi_max.jpg', is_zero=True)
kofola = Drink(name='kofola', display_name='Kofola 🇨🇿', normal_cost=40.4, discount_cost=0, image_url='images/drinks/kofola.jpg', is_zero=False)
kofola_sf = Drink(name='kofola-bez-cukru', display_name='Kofola bez cukru', normal_cost=40.4, discount_cost=0, image_url='images/drinks/kofola_sf.jpg', is_zero=True)
eiskaffee = Drink(name='ledova-kava-hochwald', display_name='EisKaffee', normal_cost=32.3, discount_cost=0, image_url='images/drinks/eiskaffee.jpg', is_zero=False)
eiskaffee_light = Drink(name='ledova-kava-light-hochwald', display_name='EisKaffee light', normal_cost=32.3, discount_cost=0, image_url='images/drinks/eiskaffee_light.jpg', is_zero=True)
monster = Drink(name='energeticky-napoj-monster-energy', display_name='Monster Energy', normal_cost=43.5, discount_cost=0, image_url='images/drinks/monster.jpg', is_zero=False)
monster_zero = Drink(name='energeticky-napoj-monster-energy-zero', display_name='Monster Energy zero sugar', normal_cost=43.5, discount_cost=0, image_url='images/drinks/monster_zero.jpg', is_zero=True)
redbull = Drink(name='energeticky-napoj-red-bull', display_name='Redbull', normal_cost=38.6, discount_cost=0, image_url='images/drinks/redbull.jpg', is_zero=False)
redbull_zero = Drink(name='energeticky-napoj-zero-red-bull', display_name='Redbull zero', normal_cost=38.6, discount_cost=0, image_url='images/drinks/redbull_zero.jpg', is_zero=True)
redbull_sf = Drink(name='energeticky-napoj-sugarfree-red-bull', display_name='Redbull sugar-free', normal_cost=38.6, discount_cost=0, image_url='images/drinks/redbull_sf.jpg', is_zero=True)
royalcrown = Drink(name='cola-royal-crown', display_name='Royal Crown cola', normal_cost=40.1, discount_cost=0, image_url='images/drinks/royalcrown.jpg', is_zero=False)
royalcrown_sf = Drink(name='cola-no-sugar-royal-crown', display_name='Royal Crown cola no sugar', normal_cost=40.1, discount_cost=0, image_url='images/drinks/royalcrown_sf.jpg', is_zero=True)
mrbrown = Drink(name='ledova-kava-mr-brown', display_name='Mr.brown coffee drink', normal_cost=63, discount_cost=0, image_url='images/drinks/mrbrown.jpg', is_zero=False)
bigshock = Drink(name='energeticky-napoj-big-shock', display_name='Big Shock', normal_cost=42, discount_cost=0, image_url='images/drinks/bigshock.jpg', is_zero=False)
bigshock_coffee = Drink(name='ledova-kava-coffee-big-shock', display_name='Big Shock coffee', normal_cost=50, discount_cost=0, image_url='images/drinks/bigshock_coffee.jpg', is_zero=False)
tiger = Drink(name='energeticky-napoj-tiger', display_name='Tiger Energy', normal_cost=33, discount_cost=0, image_url='images/drinks/tiger.jpg', is_zero=False)
rockstar = Drink(name='energeticky-napoj-rockstar', display_name='Rockstar Energy', normal_cost=38.2, discount_cost=0, image_url='images/drinks/rockstar.jpg', is_zero=False)
semtex = Drink(name='energeticky-napoj-semtex', display_name='SEMTEX', normal_cost=33.8, discount_cost=0, image_url='images/drinks/semtex.jpg', is_zero=False)
mntn_dew = Drink(name='limonada-mountain-dew', display_name='Mountain Dew' ,normal_cost=47.5, discount_cost=0, image_url='images/drinks/mntn_dew.jpg', is_zero=False)
session.add_all([cola, cola_zero, pepsi, pepsi_max, kofola, kofola_sf, eiskaffee, eiskaffee_light, monster, monster_zero, redbull, redbull_sf, redbull_zero, royalcrown, royalcrown_sf, mrbrown, bigshock, bigshock_coffee, tiger, rockstar, semtex, mntn_dew])
session.commit()
session.close()