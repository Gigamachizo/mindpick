# 뷰 및 라우트 정의
from flask import Blueprint, request, jsonify
from app.services.users import create_user
#from app.services.questions import create_question, get_all_questions
from app.services.answers import create_answer, get_answer_id
from app.services.choices import create_choice, choices_question_id
from app.services.images import create_image, get_main_image


routes_bp = Blueprint('routes', __name__)

image_id_counter = 1

# 기본 연결 획인
@routes_bp.route('/')
def service():
    return jsonify({
        "message": "Success Connect"
    })

# 메인 이미지 가져오기
@routes_bp.route('/image/main')
def image_main():
    return jsonify({"image":""})


# 회원가입
@routes_bp.route('/signup', methods=['POST'])
def signup():

    user_data = request.get_json()
    result = create_user(user_data)
    
    if 'error' in result:
        return jsonify(result), 400

    # 성공한 경우
    return jsonify(result), 201


# 질문 가져오기
@routes_bp.route('/questions/<int:question_id>')
def question_id(question_id):
    question = {
        "id": question_id,
        "title": "1번 질문입니다",
        "image": "",
        "choices": [
            { "id": 1, "content": "옵션 1", "is_active": True },
            { "id": 2, "content": "옵션 2", "is_active": True }
        ]
    }

    return jsonify(question)


#질문 개수 확인
@routes_bp.route('/questions/count')
def question_count():
    all_questions = get_main_image()
    
    return jsonify({'total': len(all_questions)})

# 선택지 가져오기
# 질문에 대한 답을 하기 위한 라우터
@routes_bp.route('/choice/<int:question_id>')
def choice(question_id):
    return choices_question_id(question_id)

# 답변 제출하기
@routes_bp.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    result = create_answer(data)

    return jsonify(result)

# 이미지 생성
@routes_bp.route('/image', methods=['POST'])
def add_image():
    data = request.get_json()
    url = create_image(data)

    new_image = {
        "id": image_id_counter,
        "url": url
    }
    images.append(new_image)
    images = get_main_image()

    response = {
        "message": f"ID: {image_id_counter} Image Success Create"
    }

    image_id_counter += 1

    return jsonify(response)

# 질문 생성
@routes_bp.route('/question', methods=['POST'])
def add_question():
    data = request.get_json()
    question_text = create_question(data)

    new_questions = {
        "question": question_text
    }
    questions.append(new_questions)

    response = {
        "message": "Title: 새로운 질문 question Success Create"
    }

    return jsonify(response)

# 선택지 생성
@routes_bp.route('/choice', methods=['POST'])
def add_choice():
    data = request.get_json()
    choice_num = create_choice(data)
    print(choice_num)
    return jsonify(choice_num)


@routes_bp.route('/answer/<int:answer_id>', methods=['GET'])
def get_answer(answer_id):
    return jsonify(get_answer_id(answer_id))