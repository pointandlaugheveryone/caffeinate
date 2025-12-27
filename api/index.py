import os, sys
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, session as flask_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio

parent_dir = str(Path(__file__).parent.parent)
sys.path.append(parent_dir)
from models import Drink
from kupi import update_prices  


app = Flask(__name__, template_folder="../templates", static_folder="../static")
load_dotenv()
DATABASE_URL=os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(bind=engine))


@app.route('/')
def get_drinks():
    drinks = db_session.query(Drink).filter_by(discount=True).all()
    return render_template('home.html', drinks=drinks, dark_mode=False)


@app.route('/zero')
def get_zero_drinks():
    zero_drinks = db_session.query(Drink).filter_by(is_zero=True, discount=True).all()
    return render_template('zeromode.html', drinks=zero_drinks, dark_mode=True)


@app.route('/about')
def about_page():
    return render_template('about.html', dark_mode=False)


def run_async_update():
    asyncio.run(update_prices())

scheduler = BackgroundScheduler()
scheduler.add_job(func=run_async_update, trigger='interval', days=1)
scheduler.start()

if __name__ == "__main__":
    app.run(debug=True)
