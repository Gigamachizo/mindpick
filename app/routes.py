# # 뷰 및 라우트 정의
from flask import request, jsonify, Blueprint
from app.sevices.users import create_user

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
    user_data = request.get_json()
    print(user_data)

    try:
         #create_user 함수 호출하여 새 사용자 생성
        new = create_user(
                name = user_data['name'], 
                age = user_data['age'], 
                gender = user_data['gender'], 
                email = user_data['email']
        )
        #새 사용자 정보 반환
        return jsonify({
            "message": f"{new.name}님 회원가입을 축하합니다",
            "user_id" : new.id
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    

