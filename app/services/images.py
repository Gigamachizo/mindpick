# images 테이블 관련 orm 함수
from flask import abort
from app.models import db, Image  # models는 여러분이 모델 정의한 파일 경로에 따라 조정하세요

# 메인 이미지 가져오기
def get_main_image() -> dict:
    img = Image.query.filter_by(type="main").first()
    if not img:
        abort(404, "메인 이미지가 없습니다.")
    return {
  "image": img.url
}

# 이미지 생성
def create_image(data: dict) -> dict:
        print("값이 들어왔니")
    #try:
        # url = data["url"]
        # image_type = data["image_type"]  # 딕셔너리 키: "type"

        # img = Image(url=url, image_type=image_type)  # image_type을 명확하게 넘겨줌


        #img = Image(url=data["url"], type=data["type"])
        img = Image(url=data["url"], image_type=data["image_type"])
        print()
        db.session.add(img)
        db.session.commit()
        return {
  "message": f"ID: {img.id} Image Success Create"
}
    # except Exception as e:
    #     abort(400, f"이미지 생성 실패: {e}")
