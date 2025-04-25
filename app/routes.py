# app/routes.py

from flask import Blueprint, jsonify, request, render_template
from app.services.users import create_user
from app.services.questions import get_question_by_id, get_question_count, create_question
from app.services.choices import get_choices_by_question_id, create_choice
from app.services.images import get_main_image, create_image
from app.services.answers import create_answer
from app.models import Answer

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/")
def personal_test():
    return render_template("index.html")

# 1. 기본 연결 확인
@routes_bp.route("/", methods=["GET"])
def health_check():
    return jsonify({"message": "Success Connect"})

# 2. 메인 이미지 가져오기
@routes_bp.route("/image/main", methods=["GET"])
def image_main():
    return jsonify(get_main_image())

# 3. 회원가입
@routes_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    return jsonify(create_user(data)), 200

# 4.1 특정 질문 가져오기
@routes_bp.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    return jsonify(get_question_by_id(question_id))

# 4.2 질문 개수 확인
@routes_bp.route("/questions/count", methods=["GET"])
def get_question_total():
    return jsonify(get_question_count())

# 5. 선택지 가져오기
@routes_bp.route("/choice/<int:question_id>", methods=["GET"])
def get_choices(question_id):
    return jsonify(get_choices_by_question_id(question_id))

# 6. 답변 제출하기
@routes_bp.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    return jsonify(create_answer(data)), 200

# 7.1 이미지 생성
@routes_bp.route("/image", methods=["POST"])
def add_image():
    data = request.get_json()
    url = data.get("url")
    image_type = data.get("image_type")
    return jsonify(create_image(url, image_type)), 200

# 7.2 질문 생성
@routes_bp.route("/question", methods=["POST"])
def add_question():
    data = request.get_json()
    return jsonify(create_question(data)), 200

# 7.3 선택지 생성
@routes_bp.route("/choice", methods=["POST"])
def add_choice():
    data = request.get_json()
    return jsonify(create_choice(data)), 200
