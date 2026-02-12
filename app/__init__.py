from dotenv import load_dotenv
from flask import Flask
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
load_dotenv()

def create_app():
    app = Flask(__name__)
    DATABASE_URL = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    engine = create_engine(DATABASE_URL)

    if not database_exists(engine.url):
        create_database(engine.url)

    from . import models
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from app.routes import routes
    app.register_blueprint(routes)

    return app
