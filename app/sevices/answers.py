from flask import abort
from models import db, Answer, Choices, User  # 필요한 모델 import
from datetime import datetime

# --- 1. 사용자의 응답 제출 ---
def create_answer(user_id, choice_id):
    # 유효성 검증 (선택지와 사용자 존재 여부)
    choice = Choices.query.get(choice_id)
    if not choice:
        abort(404, description=f"ID가 {choice_id}인 선택지를 찾을 수 없습니다.")

    user = User.query.get(user_id)
    if not user:
        abort(404, description=f"ID가 {user_id}인 사용자를 찾을 수 없습니다.")

    new_answer = Answer(user_id=user_id, choice_id=choice_id)
    db.session.add(new_answer)
    db.session.commit()
    return new_answer.to_dict()


# --- 2. ID로 단일 답변 조회 ---
def get_answer_by_id(answer_id):
    answer = Answer.query.get(answer_id)
    if not answer:
        abort(404, description=f"ID가 {answer_id}인 답변이 존재하지 않습니다.")
    return answer.to_dict()


# --- 3. 특정 사용자의 모든 답변 조회 ---
def get_answers_by_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404, description=f"ID가 {user_id}인 사용자를 찾을 수 없습니다.")

    answers = Answer.query.filter_by(user_id=user_id).all()
    return [answer.to_dict() for answer in answers]


# --- 4. 답변의 선택지 변경 ---
def update_answer_choice(answer_id, new_choice_id):
    answer = Answer.query.get(answer_id)
    if not answer:
        abort(404, description=f"ID가 {answer_id}인 답변이 존재하지 않습니다.")

    choice = Choices.query.get(new_choice_id)
    if not choice:
        abort(404, description=f"ID가 {new_choice_id}인 선택지를 찾을 수 없습니다.")

    answer.choice_id = new_choice_id
    answer.updated_at = datetime.utcnow()
    db.session.commit()
    return answer.to_dict()


# --- 5. 응답 삭제 ---
def delete_answer(answer_id):
    answer = Answer.query.get(answer_id)
    if not answer:
        abort(404, description=f"ID가 {answer_id}인 답변이 존재하지 않습니다.")
    db.session.delete(answer)
    db.session.commit()
    return {"message": f"답변 ID {answer_id}가 삭제되었습니다."}