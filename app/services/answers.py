# answers 테이블 관련 orm 함수
from flask import request, jsonify
from app.models import Answer
from config import db

# 사용자 답변 id (get)
def get_answer_id(answer_id): 
    answer = Answer.query.get(answer_id)

    if not answer:
        return {"error": "해당 ID의 답변이 존재하지 않습니다."}, 404

    answers = [{
    "id": answer.id,
    "user_id": answer.user_id,
    "choice_id": answer.choice_id
}]

    return {"answers": answers}




# POST : 사용자 답변 저장
def create_answer(data: list) -> dict:
    try:
        # data: [{ "user_id": 1, "choice_id": 2 }, { "user_id": 1, "choice_id": 4 }]
        new_answers = []

        for item in data:
            answer = Answer(
                user_id=item["user_id"],
                choice_id=item["choice_id"]
            )
            db.session.add(answer)
            new_answers.append(answer)

        db.session.commit()

        user_id = data[0]['user_id'] if data else 'Unknown'

        return {
            "message": f"User: {user_id}'s answers Success Create"
        }

    except Exception as e:
        db.session.rollback()
        print(f"Error: {str(e)}")
        return {
            "error": "답변 저장 중 오류가 발생했습니다."
        }
