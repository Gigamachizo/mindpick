from app import create_app
from config import db
from app.models import Question, Choices, Image

app = create_app()
app.app_context().push()

# 이미지 생성
img = Image(url="https://example.com/dummy.jpg", image_type="main")
db.session.add(img)
db.session.commit()

# 질문 추가
q0 = Question(title="나는 혼자있을때 더 편안함을 느낀다.", is_active=True, sqe=0, image_id=img.id)
q1 = Question(title="나는 아무 생각도 안할 수 있다.", is_active=True, sqe=1, image_id=img.id)
q2 = Question(title="누군가 나를 싫어하는 걸 알았을 때.", is_active=True, sqe=2, image_id=img.id)
q3 = Question(title="당신의 방을 깨끗한가요?", is_active=True, sqe=3, image_id=img.id)

db.session.add_all([q0, q1, q2, q3])
db.session.commit()

# 선택지 추가
c0 = Choices(question_id=q0.id, content="그렇다", is_active=True, sqe=0)
c1 = Choices(question_id=q0.id, content="아니다", is_active=True, sqe=1)
c2 = Choices(question_id=q1.id, content="그렇다", is_active=True, sqe=0)
c3 = Choices(question_id=q1.id, content="아무 생각도 안하는 생각도 생각 아닌가?", is_active=True, sqe=1)
c4 = Choices(question_id=q2.id, content="어쩌라는건지", is_active=True, sqe=0)
c5 = Choices(question_id=q2.id, content="왜 나를 싫어할까?", is_active=True, sqe=1)
c6 = Choices(question_id=q3.id, content="그렇다", is_active=True, sqe=0)
c7 = Choices(question_id=q3.id, content="아니다", is_active=True, sqe=1)

db.session.add_all([c0, c1, c2, c3, c4, c5, c6, c7])
db.session.commit()

print("✅ 질문과 선택지 삽입 완료!")
