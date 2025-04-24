# 개발환경에서 테스트 하는 실행 파일
from app import create_app

application = create_app()

if __name__ == "__main__":
    application.run(debug=True)