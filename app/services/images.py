# images 테이블 관련 orm 함수
from flask import abort
from models import db, Image  # models는 여러분이 모델 정의한 파일 경로에 따라 조정하세요

def create_image(url: str, image_type: str) -> Image:
    allowed_type = {"main", "sub"}

    if image_type not in allowed_type:
        abort(400, f"Invalid type: {image_type}. Allowed values: {allowed_type}")

    image = Image(url=url, image_type=image_type)
    db.session.add(image)
    db.session.commit()
    return image


def get_all_images() -> list[Image]:
    return Image.query.all()


def get_image_by_id(image_id: int) -> Image:
    image = Image.query.get(image_id)
    if image is None:
        abort(404, "이미지를 찾을 수 없습니다.")
    return image


def delete_image(image_id: int) -> None:
    image = get_image_by_id(image_id)
    db.session.delete(image)
    db.session.commit()
