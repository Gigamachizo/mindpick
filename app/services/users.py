# users 테이블 관련 orm 함수
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify, Blueprint
from app.models import User
from config import db

# 회원가입(POST)
def create_user(data: dict) -> dict:
    print("딕셔너리 들고 도착")
    try:
        # 새로 생성된 사용자 객체를 담는 변수
        new_user = User(
            name=data['name'],
            age=data['age'],
            gender=data['gender'],
            email=data['email']
        )
        print(new_user)
        
        
        # DB에 새 사용자 객체 추가 및 커밋
        db.session.add(new_user)
        db.session.commit()

        print(new_user)
        
        # 성공적인 사용자 생성 후 반환할 메시지
        return {
            "message": f"{new_user.name}님 회원가입을 축하합니다",
            "user_id": new_user.id
        }
    
    except IntegrityError as e:
        # 중복된 이메일 오류 등의 예외 처리
        db.session.rollback()  # 롤백
        print(f"Error: {str(e)}")
        return {
            "error": "이미 존재하는 이메일입니다."
        }
