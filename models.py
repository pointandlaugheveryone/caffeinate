import os
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False, unique=True)
    display_name = Column(String(500), nullable=False)
    logo_url = Column(String(500), nullable=False)


class Drink(Base):
    __tablename__ = 'drinks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False, unique=True)
    display_name = Column(String(500), nullable=False, unique=True)
    discount_cost = Column(Float, nullable=False)
    image_url = Column(String(200))
    is_zero = Column(Boolean, default=False)
    discount = Column(Boolean, default=False)
    offered_amount = Column(String(100))

    store_id = Column(Integer, ForeignKey('stores.id'))
    store = relationship('Store')


DATABASE_URL=os.getenv('DATABASE_URL_UNPOOLED')
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()