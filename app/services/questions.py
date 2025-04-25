from flask import abort
from app.models import Question, db, Image, Choices


# 조회
def get_question_by_id(question_id: int) -> dict:
    question = Question.query.get_or_404(question_id)
    return {
        "id": question.id,
        "title": question.title,
        "image": question.image.url if question.image else "",
        "choices": [
            {
                "id": c.id,
                "content": c.content,
                "is_active": c.is_active
            } for c in Choices.query.filter_by(question_id=question_id).all()
        ]
    }

# 질문 수
def get_question_count() -> dict:
    total = Question.query.count()
    return {"total": total}

# 생성
def create_question(data: dict) -> dict:
    new_question = Question(
        title=data["title"],
        is_active=True,
        sqe=data["sqe"],
        image_id=data["image_id"]
    )
    db.session.add(new_question)
    db.session.commit()
    return {"message": "Title: 새로운 질문 question Success Create"}
