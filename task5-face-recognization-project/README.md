# Face Detection and Recognition System

## 📋 Project Overview
This is a **Real-time Face Detection and Recognition** application developed using Python for my Internship. It can detect faces from webcam/video and recognize known persons with their names.

## ✨ Features
- Real-time face detection from webcam
- Face recognition with name display
- Green box for recognized persons, Red box for Unknown
- Fast performance (frame resizing)
- Automatic saving of face encodings
- Screenshot saving (Press 'S')
- Press 'Q' to quit

## 🛠 Technologies Used
- Python 3.10
- OpenCV
- face_recognition (dlib)
- NumPy
- Pickle

## 📁 Project Structure
face-recognition-project/
├── known_faces/              # One folder per person
│   ├── Hamsini/
│   ├── Priyanka/
│   └── ...
├── test_images/              # Test photos
├── final_app.py              # Main file
├── known_encodings.pkl       # Auto generated
├── README.md
└── requirements.txt
text## 🚀 How to Setup and Run

1. **Install Libraries**
   ```bash
   pip install opencv-python face_recognition numpy pillow

Add Known Faces
Create folders inside known_faces (example: known_faces/Hamsini)
Add 5-10 clear front-facing photos in each person's folder

Run the ApplicationBash by:-  python final_app.py

📸 How to Use

Run the program, webcam will start
Stand in front of camera
Name will appear if person is recognized
Press S → Save screenshot
Press Q → Quit

## 🌐 Web Interface (Streamlit)

Run the web version:
```bash
streamlit run app.py
or
 python -m streamlit run app.py
🔧 Adding New Person

Create new folder in known_faces
Add 5-10 good photos
Delete known_encodings.pkl file
Run final_app.py again

⚡ Future Improvements

Web interface using Streamlit
Attendance marking system
Add new face from webcam
Better accuracy with deep learning models