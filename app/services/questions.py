# quetions 테이블 관련 orm 함수

# questions  질문하기 위해 get 
# choices 사용자가 선택 Post
# answer 답변 get/answers get/answers/{id}
# from app.models import Question

# def get_all_questions(data:dict)->dict:
#     questions = Question.query.all()
#     question_list = []

#     for q in questions:
#             question_list.append({
#                 "id": q.id,
#                 "question_text": q.question_text
#             })

#     return {"questions": question_list}


