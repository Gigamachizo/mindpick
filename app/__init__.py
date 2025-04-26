# 앱 초기화 및 설정 파일
from flask import Flask
from config import db
from flask_migrate import Migrate
from app.routes import routes_bp

import app.models

# Migrate 객체를 전역 변수로 선언
migrate = Migrate()

# 팩토리 패턴
def create_app():
    # Flask 객체 생성 # 지역변수
    application = Flask(__name__)

    # 환경 설정 로드
    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    # DB, 마이그레이션 초기화
    db.init_app(application)
    migrate.init_app(application, db)

    # 블루 프린트 등록
    application.register_blueprint(routes_bp)

    return application
