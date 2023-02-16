import face_recognition
import numpy as np


known_encodings = []
known_name = ["박소담", "김고은"]

# 김고은
kim = face_recognition.load_image_file(f"kimge/001.jpg")
known_encodings.append(face_recognition.face_encodings(kim)[0])

#박소담
park = face_recognition.load_image_file(f"parksd/001.jpg")
known_encodings .append(face_recognition.face_encodings(park)[0])

#모르는사람
unknown = face_recognition.load_image_file("002.jpg")
unknown_encoding = face_recognition.face_encodings(unknown)[0]


distances = face_recognition.face_distance(
    known_encodings, unknown_encoding
)

#print(distances)
min_distance = np.argmin()
#print(distances[min_distance])
#print(known_name[min_distance])

if min_distance < 0.5:
    print("몰라")
else:
    print(known_name[min_distance])