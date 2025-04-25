from app.models import Answer, db
from flask import abort

def create_answer(data: list) -> dict:
    for item in data:
        user_id = item.get("user_id")
        choice_id = item.get("choice_id")
        if not user_id or not choice_id:
            abort(400, "user_id와 choice_id는 필수입니다.")
        answer = Answer(user_id=user_id, choice_id=choice_id)
        db.session.add(answer)
    db.session.commit()
    return {"message": f"User: {data[0]['user_id']}'s answers Success Create"}
