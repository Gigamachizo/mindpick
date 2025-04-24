# 뷰 및 라우트 정의
from flask import Flask, jsonify, request

app = Flask(__name__)




@app.route('/')
def service():
    return jsonify({
        "message": "Success Connect"
    })


@app.route('/image/main')
def image_main():
    return jsonify({"image":""})


users = []
@app.route('/signup', methods=['POST'])
def signup():

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    age = data.get('age')
    gender = data.get('gender')

    for user in users:
        if user['email'] == email:
            return jsonify({"message":"이미 존재하는 계정 입니다."}),

    new_user = {
        "name": name,
        "email": email,
        "age": age,
        "gender": gender
    }
    users.append(new_user)

    response = {
        "message": f"{name}님 회원가입을 축하합니다",
        "user_id": 1
    }
    
    return jsonify(response),

@app.route('/questions/<int:question_id>')
def question_id():
    question = {
        "id": 1,
        "title": "1번 질문입니다",
        "image": "",
        "choices": [
            { "id": 1, "content": "옵션 1", "is_active": True },
            { "id": 2, "content": "옵션 2", "is_active": True }
        ]
    }

    return jsonify(question)

@app.route('/questions/count')
def question_count():
    total = len(questions)
    
    return jsonify({'total': total})


@app.route('/choice/<int:question_id>')
def choice():
    choice = {
        "choices": [
        { "id": 1, "content": "옵션 1", "is_active": true },
        { "id": 2, "content": "옵션 2", "is_active": true }
        ]
    }
    return jsonify(choice)

user_answers = []
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_id = data.get('user_id')
    answers = data.get('answers')

    user_answers.append({
        "user_id": user_id,
        "answers": answers
    })

    return jsonify({"message": f"user: {user_id}'s answer  Create"})

images = []
image_id_counter = 1
@app.route('/image', methods=['POST'])
def add_image():
    data = request.get_json()
    url = data.get('url')

    new_image = {
        "id": image_id_counter,
        "url": url
    }
    images.append(new_image)

    response = {
        "message": f"ID: {image_id_counter} Image Success Create"
    }

    image_id_counter += 1

    return jsonify(response)

questions = []
@app.route('/question', methods=['POST'])
def add_question():
    data = request.get_json()
    question_text = data.get('question')

    new_questions = {
        "question": question_text
    }
    questions.append(new_questions)

    response = {
        "message": "Title: 새로운 질문 question Success Create"
    }

    return jsonify(response)

choices = []
@app.route('/choice', methods=['POST'])
def add_choice():
    data = request.get_json()
    choice_num = data.get('choice')

    new_choice = {
        'choice': choice_num
    }
    choices.append(new_choice)

    response = {
        "message": "Content: 새로운 선택지 choice Success Create"
    }

    return jsonify(response)

if __name__ == "__main--":
    app.run(debug=True)