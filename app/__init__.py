from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.api import app as api_blueprint
    from app.dashboard import app as dashboard_blueprint

    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(dashboard_blueprint, url_prefix='/')

    return app