# choices 테이블 관련 orm 함수
from flask import jsonify
from app.models import Choices
from app.models import db, Question
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

#POST
def create_choice(data: dict) -> dict:
    print("딕셔너리 들고 도착")
    try:
        new_choice = Choices(
            question_id=data['question_id'],
            content=data['content'],
            is_active=data['is_active'],
            sqe=data['sqe']
        )

        db.session.add(new_choice)
        db.session.commit()

        return {
            "message": "Content: 새로운 선택지 choice Success Create"
        }
    
    except IntegrityError:
        db.session.rollback()
        raise

#GET #데이터베이스에서 조회
def choices_question_id(question_id):
    question = Question.query.get(question_id)

    if not question:
        return {"error":"해당 ID의 질문이 존재하지 않습니다"}
    

    # 각 정보 딕션너리 형태로 반환 및 리스트 추가
        # 선택지 가져오기
    choices = []
    for choice in question.choices:  # 이제 question.choices가 작동할 것입니다.
        choices.append({
            "id": choice.id,
            "content": choice.content,
            "is_active": choice.is_active
        })

    # 원하는 형태로 응답 반환
    return {"choices": choices}



    #  # 선택지 가져오기
    # choices = Choices.query.filter_by(question_id=question.id).all()

    # # 선택지 리스트 반환
    # choices_list = [choice.to_dict() for choice in choices]

    # return jsonify({"choices": choices_list})




 


