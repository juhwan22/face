import dlib
import os
import shutil


# 디렉터리 삭제
if os.path.exists("filtering_02"):
        shutil.rmtree("filtering_02")


# 디렉터리 생성
if not os.path.exists("filtering_02"):
        os.makedirs("filtering_02")

detector = dlib.get_frontal_face_detector()
files = os.listdir("kimge")
for file in files:
    try:
        img_rgb = dlib.load_rgb_image(f"kimge/{file}")
        faces = detector(img_rgb)
        print(f"{file} => {len(faces)}개 찾음")

        if len(faces) == 1:
            shutil.copy(f"kimge/{file}", f"filtering_02/{file}")
    except:
        pass

