# users 테이블 관련 orm 함수

from flask import abort, session
from models import db, User


# 1. 회원가입
def create_user(data):
    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")
    email = data.get("email")

    if not all([name, age, gender, email]):
        abort(400, description="필수 입력값(name, age, gender, email)이 누락되었습니다.")

    # 이메일 중복 체크
    if User.query.filter_by(email=email).first():
        abort(409, description="이미 등록된 이메일입니다.")

    try:
        user = User(name=name, age=age, gender=gender, email=email)
        db.session.add(user)
        db.session.commit()
        return user.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"사용자 생성 중 오류가 발생했습니다: {str(e)}")


# 2. 로그인 (간단한 세션 기반)
def login_user(data):
    email = data.get("email")

    if not email:
        abort(400, description="이메일이 필요합니다.")

    user = User.query.filter_by(email=email).first()
    if not user:
        abort(404, description="해당 이메일의 사용자를 찾을 수 없습니다.")

    # 로그인 성공 → 세션에 저장
    session['user_id'] = user.id
    return {"message": "로그인 성공", "user": user.to_dict()}


# 3. 프로필 조회
def get_user_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="사용자를 찾을 수 없습니다.")
    return user.to_dict()


# 4. 사용자 정보 수정
def update_user(user_id, data):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="사용자를 찾을 수 없습니다.")

    user.name = data.get("name", user.name)
    user.age = data.get("age", user.age)
    user.gender = data.get("gender", user.gender)
    user.email = data.get("email", user.email)

    try:
        db.session.commit()
        return user.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"수정 중 오류가 발생했습니다: {str(e)}")


# 5. 사용자 삭제
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description="사용자를 찾을 수 없습니다.")

    db.session.delete(user)
    db.session.commit()
    session.pop('user_id', None)  # 세션도 제거

    return {"message": f"사용자 ID {user_id}가 삭제되었습니다."}