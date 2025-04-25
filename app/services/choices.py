# choices 테이블 관련 orm 함수

from flask import abort
from models import db, Choices, Question


# 선택지 생성
def create_choice(data):
    content = data.get("content")
    sqe = data.get("sqe")
    is_active = data.get("is_active", True)
    question_id = data.get("question_id")

    # 필수값 확인
    if not all([content, isinstance(sqe, int), question_id]):
        abort(400, description="필수 값(content, sqe, question_id)이 누락되었거나 유효하지 않습니다.")

    # 질문 존재 여부 확인
    question = Question.query.get(question_id)
    if not question:
        abort(404, description=f"ID가 {question_id}인 질문을 찾을 수 없습니다.")

    # Choice 객체 생성
    choice = Choices(
        content=content,
        sqe=sqe,
        is_active=is_active,
        question_id=question_id
    )

    db.session.add(choice)
    db.session.commit()

    return choice.to_dict()


# 특정 질문에 대한 선택지 목록 조회
def get_choices_by_question(question_id):
    question = Question.query.get(question_id)
    if not question:
        abort(404, description=f"ID가 {question_id}인 질문을 찾을 수 없습니다.")

    choices = Choices.query.filter_by(question_id=question_id).order_by(Choices.sqe).all()
    return [choice.to_dict() for choice in choices]