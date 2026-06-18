import cv2
import face_recognition
import os
import pickle

# ================== CONFIG ==================
KNOWN_FACES_DIR = "known_faces"
ENCODINGS_FILE = "known_encodings.pkl"
TOLERANCE = 0.60

# Load or create encodings
if os.path.exists(ENCODINGS_FILE):
    with open(ENCODINGS_FILE, "rb") as f:
        known_encodings = pickle.load(f)
    print("✅ Loaded from file:", list(known_encodings.keys()))
else:
    known_encodings = {}
    print("Loading known faces...")
    for person in os.listdir(KNOWN_FACES_DIR):
        person_dir = os.path.join(KNOWN_FACES_DIR, person)
        if os.path.isdir(person_dir):
            encodings = []
            for img_file in os.listdir(person_dir):
                try:
                    img_path = os.path.join(person_dir, img_file)
                    image = face_recognition.load_image_file(img_path)
                    enc = face_recognition.face_encodings(image)
                    if enc:
                        encodings.append(enc[0])
                except:
                    pass
            if encodings:
                known_encodings[person] = encodings
    with open(ENCODINGS_FILE, "wb") as f:
        pickle.dump(known_encodings, f)
    print("✅ Saved encodings:", list(known_encodings.keys()))

# ================== WEBCAM ==================
video_capture = cv2.VideoCapture(0)
print("🎥 Webcam Started - Press 'q' to Quit")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        name = "Unknown"
        for person, encodings in known_encodings.items():
            matches = face_recognition.compare_faces(encodings, face_encoding, tolerance=TOLERANCE)
            if True in matches:
                name = person
                break

        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Recognition System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
print("✅ Stopped")