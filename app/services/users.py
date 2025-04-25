from flask import abort
from app.models import User, db

# 유저 생성
def create_user(data):
    try:
        user = User(
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            email=data["email"]
        )
    except Exception as e:
        abort(400, f"회원 생성 실패: {e}")

    db.session.add(user)
    db.session.commit()
    return {
        "message": f"{user.name}님 회원가입을 축하합니다!",
        "user_id": user.id
    }