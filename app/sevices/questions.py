# questions 테이블 관련 orm 함수

from flask import abort
from models import db, Question, Image


# 1. 설문조사(질문) 생성
def create_question(data):
    title = data.get("title")
    sqe = data.get("sqe")
    image_id = data.get("image_id")
    is_active = data.get("is_active", True)

    if not all([title, sqe, image_id]):
        abort(400, description="필수 값(title, sqe, image_id)이 누락되었습니다.")

    if not isinstance(title, str) or not title.strip():
        abort(400, description="title은 빈 문자열일 수 없습니다.")

    if not isinstance(sqe, int):
        abort(400, description="sqe는 정수이어야 합니다.")

    image = Image.query.get(image_id)
    if not image:
        abort(404, description=f"ID가 {image_id}인 이미지를 찾을 수 없습니다.")

    existing = Question.query.filter_by(title=title).first()
    if existing:
        abort(409, description="동일한 제목의 질문이 이미 존재합니다.")

    question = Question(title=title, sqe=sqe, image_id=image_id, is_active=is_active)
    db.session.add(question)
    db.session.commit()

    return question.to_dict()


# 2. 단일 질문 조회
def get_question(question_id):
    question = Question.query.get(question_id)
    if not question:
        abort(404, description=f"ID가 {question_id}인 질문을 찾을 수 없습니다.")
    return question.to_dict()


# 3. 설문조사 전체 개수 확인
def get_question_count():
    count = Question.query.count()
    return {"total_questions": count}


# 4. 설문조사(질문) 수정
def update_question(question_id, data):
    question = Question.query.get(question_id)
    if not question:
        abort(404, description=f"ID가 {question_id}인 질문을 찾을 수 없습니다.")

    title = data.get("title", question.title)
    sqe = data.get("sqe", question.sqe)
    image_id = data.get("image_id", question.image_id)
    is_active = data.get("is_active", question.is_active)

    if not isinstance(title, str) or not title.strip():
        abort(400, description="title은 빈 문자열일 수 없습니다.")
    if not isinstance(sqe, int):
        abort(400, description="sqe는 정수이어야 합니다.")

    if image_id:
        image = Image.query.get(image_id)
        if not image:
            abort(404, description=f"ID가 {image_id}인 이미지를 찾을 수 없습니다.")

    question.title = title
    question.sqe = sqe
    question.image_id = image_id
    question.is_active = is_active

    db.session.commit()
    return question.to_dict()


# 5. 설문조사(질문) 삭제
def delete_question(question_id):
    question = Question.query.get(question_id)
    if not question:
        abort(404, description=f"ID가 {question_id}인 질문을 찾을 수 없습니다.")

    db.session.delete(question)
    db.session.commit()
    return {"message": f"질문 ID {question_id}가 삭제되었습니다."}
