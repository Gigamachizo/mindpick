# 앱 초기화 및 설정 파일
# app/__init__.py

from config import db
from flask import Flask
from flask_migrate import Migrate

import app.models
from app.routes import routes_bp  #routes.py에서 Blueprint 가져오기

migrate = Migrate()

def create_app():
    application = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
        )
    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)
    migrate.init_app(application, db)

    from app.routes import routes_bp
    application.register_blueprint(routes_bp, url_prefix="/api")

    return application


