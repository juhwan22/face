# 02.opencv_find_one_person.py
# pip install opencv-contrib-python

import os
import cv2
import shutil



# 디렉터리 삭제
if os.path.exists("filtering_01"):
        shutil.rmtree("filtering_01")


# 디렉터리 생성
if not os.path.exists("filtering_01"):
        os.makedirs("filtering_01")


detector = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml")
files = os.listdir("kimge")
for file in files:
    try:
        img_bgr = cv2.imread(f"kimge/{file}")
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(img_gray)
        print(f"{file} => {len(faces)}개 찾음")

        if len(faces) == 1:
            shutil.copy(f"kimge/{file}", f"filtering_01/{file}")
    except:
        pass