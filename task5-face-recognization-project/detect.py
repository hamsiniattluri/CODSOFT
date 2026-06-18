import cv2
import face_recognition

# Change this to your image name
image_path = "test_images/test1.jpg"

# Load the image
image = face_recognition.load_image_file(image_path)

# Detect faces
face_locations = face_recognition.face_locations(image)

print(f"✅ Found {len(face_locations)} face(s) in the image!")

# Draw green boxes using OpenCV
img = cv2.imread(image_path)
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 4)

# Show the image
cv2.imshow("Face Detection", img)
cv2.waitKey(0)          # Press any key to close window
cv2.destroyAllWindows()