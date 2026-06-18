import streamlit as st
import cv2
import face_recognition
import os
import pickle
from PIL import Image
import numpy as np

st.set_page_config(page_title="Face Recognition System", layout="wide")
st.title("🧑‍🤝‍🧑 Face Detection & Recognition System")
st.markdown("### Internship Project")

# Load encodings
@st.cache_data
def load_encodings():
    if os.path.exists("known_encodings.pkl"):
        with open("known_encodings.pkl", "rb") as f:
            return pickle.load(f)
    return {}

known_encodings = load_encodings()

st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose Mode", ["Webcam Live", "Upload Image"])

TOLERANCE = st.sidebar.slider("Recognition Tolerance", 0.4, 0.7, 0.60)

if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        
        face_locations = face_recognition.face_locations(img_array)
        face_encodings = face_recognition.face_encodings(img_array, face_locations)
        
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        for (top, right, bottom, left), face_enc in zip(face_locations, face_encodings):
            name = "Unknown"
            for person, encodings in known_encodings.items():
                if True in face_recognition.compare_faces(encodings, face_enc, tolerance=TOLERANCE):
                    name = person
                    break
            
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(img_bgr, (left, top), (right, bottom), color, 3)
            cv2.putText(img_bgr, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)
        
        st.image(img_bgr, channels="BGR", caption="Result", use_column_width=True)

elif option == "Webcam Live":
    st.info("Webcam mode works better in the desktop version. For now use Upload Image or run final_app.py")
    st.warning("For real-time webcam in Streamlit, it's a bit tricky. We'll use it for image upload mainly.")

st.sidebar.markdown("---")
st.sidebar.info("Add more photos in `known_faces` folder and delete `known_encodings.pkl` to update.")

st.caption("Made for Internship | Face Recognition Project")