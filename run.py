# 개발환경에서 테스트 하는 실행 파일
from app import create_app 
from config import db

# create_app() 함수 호출
application = create_app()

# 서버 시작 시에 한번만 테이블이 생성됩니다.
with application.app_context():
    #db.drop_all()
    db.create_all()

if __name__ == "__main__":
    application.run(debug=True)