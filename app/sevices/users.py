# users 테이블 관련 orm 함수
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify, Blueprint
from app.models import User
from config import db

# 회원가입(POST)
def create_user(name, age, gender, email):
    #새로 생성된 사용자 객체를 담는 변수
    #User, db.Model을 상속받은 클래스
    new_user = User(
            name=name,
            age=age,
            gender=gender,
            email=email
        )
    
    db.session.add(new_user)
    db.session.commit()

    return new_user



    

 
