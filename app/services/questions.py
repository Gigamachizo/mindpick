# questions 테이블 관련 orm 함수
from flask import abort
from models import Question, Choice, Answer  # 모델 클래스 직접 import

def get_question_detail(question_id):
    question = Question.query.get(question_id)
    if not question:
        abort(404, description=f"ID가 {question_id}인 질문을 찾을 수 없습니다.")

    choices = Choice.query.filter_by(question_id=question_id, is_active=True).all()
    choices_data = [
        {
            "id": choice.id,
            "content": choice.content,
            "is_active": choice.is_active
        }
        for choice in choices
    ]

    total_answers = Answer.query \
        .join(Choice, Answer.choice_id == Choice.id) \
        .filter(Choice.question_id == question_id) \
        .count()

    return {
        "id": question.id,
        "title": question.title,
        "image": question.image,
        "choices": choices_data,
        "total": total_answers
    }
