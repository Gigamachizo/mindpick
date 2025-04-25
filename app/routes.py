# # 뷰 및 라우트 정의
from flask import request, jsonify, Blueprint
from app.services.users import create_user

# Blueprint 생성
main_blp = Blueprint('Main', __name__, url_prefix='/main')
user_blp = Blueprint('Users', __name__, url_prefix='/users')

#기본 연결 확인
@main_blp.route('/', methods = ['GET'])
def index():
    print("GET 요청 통과")
    return jsonify({"message": "Success Connect"})

#회원가입
@user_blp.route('/', methods = ['POST'])
# 회원가입(POST)
def post():
    print("라우트에 요청 도착")
    data = request.get_json()  # 클라이언트에서 보낸 JSON 데이터
    
    # 사용자 생성 함수 호출
    users = create_user(data)
    
    # 에러가 발생한 경우, 400 상태 코드와 함께 반환
    if 'error' in users:
        return jsonify(users), 400  # 에러 응답을 반환
    
    # 성공적으로 생성된 사용자 정보 반환
    return jsonify(users), 201  # 성공 시 201 상태 코드와 함께 반환

