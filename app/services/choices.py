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
            "message": f"Content: {new_choice.content} choice Success Create"
        }
    
    except IntegrityError:
        db.session.rollback()
        raise


#GET <id>
def choices_question_id(question_id: int) -> dict:
    choices = Choices.query.filter_by(question_id=question_id).all()
    return {
        "choices": [
            {
                "id": c.id,
                "content": c.content,
                "is_active": c.is_active
            } for c in choices
        ]
    }






 


