from flask import Flask, render_template, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from apscheduler.schedulers.background import BackgroundScheduler

from config import DATABASE_URL
from models import Drink
from kupi import update_prices  


app = Flask(__name__)

engine = create_engine(DATABASE_URL)
session = scoped_session(sessionmaker(bind=engine))


@app.route('/')
def get_drinks():
    drinks = session.query(Drink).filter_by(discount=True).all()
    return render_template('home.html', drinks=drinks, dark_mode=False)


@app.route('/zero')
def get_zero_drinks():
    zero_drinks = session.query(Drink).filter_by(is_zero=True, discount=True).all()
    return render_template('zeromode.html', drinks=zero_drinks, dark_mode=True)


@app.route('/about')
def about_page():
    return render_template('about.html', dark_mode=False)


# fetch prices daily
scheduler = BackgroundScheduler()
scheduler.add_job(func=update_prices, trigger='interval', days=1)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
