import cv2
import face_recognition
import os

KNOWN_FACES_DIR = "known_faces"

# Load known faces
known_encodings = {}
for person in os.listdir(KNOWN_FACES_DIR):
    person_dir = os.path.join(KNOWN_FACES_DIR, person)
    encodings = []
    for img_file in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_file)
        image = face_recognition.load_image_file(img_path)
        enc = face_recognition.face_encodings(image)
        if enc:
            encodings.append(enc[0])
    if encodings:
        known_encodings[person] = encodings

print("✅ Known faces loaded:", list(known_encodings.keys()))

# Test on image
image_path = "test_images/test2.jpg"
image = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

img = cv2.imread(image_path)

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    name = "Unknown"
    for person, encodings in known_encodings.items():
        matches = face_recognition.compare_faces(encodings, face_encoding, tolerance=0.55)
        if True in matches:
            name = person
            break
    
    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
    cv2.putText(img, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow("Face Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()