# questions 테이블 관련 orm 함수
from flask import abort 
from app.models import Question, Choices, db  # 모델 클래스 직접 import

# 특정 질문과 선택지 조회
def get_question_detail(question_id):
    print("여기 값 찍히지?")
    question = Question.query.get(question_id)
    
    return {
        "id": question.id,
        "title": question.title,
        "image": question.image.url if question.image else "",
        "choices": [
            { "id": c.id, "content": c.content, "is_active": c.is_active }for c in Choices.query.filter_by(question_id = question_id).all()
            ]

    }

# 질문 수 조회
def get_question_count():
    total = Question.query.count()
    print(total)
    return {
        "total": total
    }

# 질문 생성 
def create_question(d):
        create_q = Question(
                    title = d["title"],
                    is_active = d.get("is_active"),
                    sqe =d["sqe"],
                    image_id = d["image_id"],

                )
        
        db.session.add(create_q)
        db.session.commit()
        return {
             "message": f"Title: {create_q.title} question Success Create"
        }

