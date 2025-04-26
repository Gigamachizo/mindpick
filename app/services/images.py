# images 테이블 관련 orm 함수
from flask import abort
from app.models import Image, db

# 메인 이미지 가져오기
def get_main_image() -> dict:
    main_image = Image.query.filter_by(type="main").first()
    if not main_image:
        abort(404, "메인 이미지가 없습니다.")
    return {"image": main_image.url} .id

# 이미지 생성
def create_image(url: str, image_type: str) -> dict:
    try:
        new_image = Image(url=url, image_type=image_type)  # ❗여기서 abort 발생 가능
    except Exception as e:
        abort(400, f"이미지 생성 중 오류 발생: {str(e)}")

    db.session.add(new_image)
    db.session.commit()
    return {"message": f"ID: {new_image.id} Image Success Create"}