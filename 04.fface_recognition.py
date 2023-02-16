import cv2
import face_recognition
import imutils

image = face_recognition.load_image_file("001.jpg")
image_bgr = imutils.resize(image, width=800)
face_locations = face_recognition.face_locations(image)


for face_locations in face_locations:
    top, right, bottom, left = face_locations
    cv2.rectangle(image, (left, bottom), (right, top), (255, 0, 0),1)
    print(face_locations)
# print(face_locations)


# RGB -> BGR
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow("face", image_bgr)
cv2.waitKey(0)
cv2.destroyWindow()















