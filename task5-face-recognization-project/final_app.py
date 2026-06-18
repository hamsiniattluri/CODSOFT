import cv2
import face_recognition
import os
import pickle
import datetime

# ============= CONFIG =============
KNOWN_FACES_DIR = "known_faces"
ENCODINGS_FILE = "known_encodings.pkl"
TOLERANCE = 0.60

# Load or Train encodings
if os.path.exists(ENCODINGS_FILE):
    with open(ENCODINGS_FILE, "rb") as f:
        known_encodings = pickle.load(f)
    print(f"✅ Loaded {len(known_encodings)} persons")
else:
    known_encodings = {}
    print("Training new faces...")
    for person in os.listdir(KNOWN_FACES_DIR):
        person_dir = os.path.join(KNOWN_FACES_DIR, person)
        if os.path.isdir(person_dir):
            encodings = []
            for img_file in os.listdir(person_dir):
                try:
                    image = face_recognition.load_image_file(os.path.join(person_dir, img_file))
                    enc = face_recognition.face_encodings(image)
                    if enc:
                        encodings.append(enc[0])
                except:
                    pass
            if encodings:
                known_encodings[person] = encodings
                print(f"   Trained: {person} ({len(encodings)} photos)")
    with open(ENCODINGS_FILE, "wb") as f:
        pickle.dump(known_encodings, f)

print("🎯 Ready Persons:", list(known_encodings.keys()))

# ============= WEBCAM =============
cap = cv2.VideoCapture(0)
print("🎥 Camera Started | Press 'q' to Quit | Press 's' to Save Screenshot")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for (top, right, bottom, left), face_enc in zip(face_locations, face_encodings):
        name = "Unknown"
        for person, encodings in known_encodings.items():
            if True in face_recognition.compare_faces(encodings, face_enc, tolerance=TOLERANCE):
                name = person
                break

        top, right, bottom, left = [x * 4 for x in (top, right, bottom, left)]

        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Show date & time
    cv2.putText(frame, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Face Recognition System - Internship Project", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f"screenshot_{datetime.datetime.now().strftime('%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Screenshot saved: {filename}")

cap.release()
cv2.destroyAllWindows()
print("✅ Program Stopped")