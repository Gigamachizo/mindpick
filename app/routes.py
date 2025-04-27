# 뷰 및 라우트 정의
from flask import Blueprint, request, jsonify
from app.services.users import create_user
from app.services.questions import create_question, get_question_detail, get_question_count
from app.services.answers import create_answer
from app.services.choices import create_choice, get_choices_question_id
from app.services.images import create_image, get_main_image


routes_bp = Blueprint('routes', __name__)

image_id_counter = 1

# 1.기본 연결 획인
@routes_bp.route('/')
def service():
    return jsonify({
        "message": "Success Connect"
    })

# 2.메인 이미지 가져오기
@routes_bp.route('/image/main', methods=['GET'])
def get_main_img():
    main_img = get_main_image()
    return jsonify(main_img)


# 3.회원가입
@routes_bp.route('/signup', methods=['POST'])
def signup():
    user_data = request.get_json()
    result = create_user(user_data)
    return jsonify(result), 201

# 4-1.질문 가져오기
@routes_bp.route('/questions/<int:question_id>')
def get_question(question_id):
    return get_question_detail(question_id)

# 4-2.질문 개수 확인
@routes_bp.route('/questions/count')
def question_count():
    all_questions = get_question_count()
    
    return jsonify({'total': len(all_questions)})

# 5. 선택지 가져오기
@routes_bp.route('/choice/<int:question_id>')
def choice(question_id):
    return get_choices_question_id(question_id)

# 6. 답변 제출하기
@routes_bp.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    result = create_answer(data)

    return jsonify(result)

# 7-1. 이미지 생성 (보류)
@routes_bp.route('/image', methods=['POST'])
def add_image():
    data = request.get_json()
    url = create_image(data)

    return jsonify(url)

# 7-2. 질문 생성
@routes_bp.route('/question', methods=['POST'])
def add_question():
    data = request.get_json()
    question_text = create_question(data)

    return jsonify(question_text)

# 7-3. 선택지 생성
@routes_bp.route('/choice', methods=['POST'])
def add_choice():
    data = request.get_json()
    choice_num = create_choice(data)
    print(choice_num)
    return jsonify(choice_num)

# (보류)
# @routes_bp.route('/answer/<int:answer_id>', methods=['GET'])
# def get_answer(answer_id):
#     return jsonify(get_answer_id(answer_id))
