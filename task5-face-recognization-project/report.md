# Internship Project Report
## Face Detection and Recognition System

### 1. Project Title
Real-time Face Detection and Recognition using Python

### 2. Objective
To develop a system that can detect faces in real-time and recognize known persons from webcam.

### 3. Technologies Used
- Python 3.10
- OpenCV
- face_recognition library (dlib)
- NumPy

### 4. Features Implemented
- Real-time face detection
- Face recognition with name tagging
- Different color boxes (Green = Known, Red = Unknown)
- Fast processing using frame resizing
- Encoding saving using Pickle
- Screenshot saving feature

### 5. How It Works
- Face encodings (128D vectors) are created from known photos
- Live webcam frames are compared with known encodings using Euclidean distance
- Tolerance = 0.60 for matching

### 6. Project Structure
(See README.md for details)

### 7. Screenshots
- [Attach Screenshot 1: Hamsini recognized]
- [Attach Screenshot 2: Priyanka recognized]
- [Attach Screenshot 3: Unknown person]
- [Attach Screenshot 4: Full working window]

### 8. Challenges Faced & Solutions
- Installation of dlib → Installed Visual Studio Build Tools
- Unknown recognition → Added more photos + adjusted tolerance
- Slow webcam → Resized frame to 1/4 size

### 9. Future Scope
- Web GUI using Streamlit
- Attendance management system
- Emotion detection
- Use better models like ArcFace

### 10. Conclusion
Successfully developed a working real-time face recognition system. This project helped me learn computer vision basics and Python libraries.

Submitted by: Hamsini Attluri   
10-06-2026