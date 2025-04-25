from flask import abort
from app.models import Choices, db

def get_choices_by_question_id(question_id: int) -> dict:
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

def create_choice(data: dict) -> dict:
    new_choice = Choices(
        content=data["content"],
        is_active=data.get("is_active", True),
        sqe=data["sqe"],
        question_id=data["question_id"]
    )
    db.session.add(new_choice)
    db.session.commit()
    return {"message": "Content: 새로운 선택지 choice Success Create"}
