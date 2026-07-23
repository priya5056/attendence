
import dlib
import numpy as np
import face_recognition_models
import streamlit as st

from sklearn.svm import SVC

from src.database.db import get_all_students


# -------------------------------
# Load Dlib Models (Loads only once)
# -------------------------------
@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()

    shape_predictor = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    face_encoder = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, shape_predictor, face_encoder


# -------------------------------
# Generate 128-D Face Embeddings
# -------------------------------
def get_face_embeddings(image_np):
    detector, shape_predictor, face_encoder = load_dlib_models()

    faces = detector(image_np, 1)

    embeddings = []

    for face in faces:
        shape = shape_predictor(image_np, face)

        descriptor = face_encoder.compute_face_descriptor(
            image_np,
            shape,
            1
        )

        embeddings.append(np.array(descriptor))

    return embeddings


# -------------------------------
# Train Face Recognition Model
# -------------------------------
@st.cache_resource
def get_trained_model():

    students = get_all_students()

    if not students:
        return None

    X = []
    y = []

    for student in students:

        embedding = student.get("face_embedding")

        if embedding is None:
            continue

        X.append(np.array(embedding))
        y.append(student["student_id"])

    if len(X) == 0:
        return None

    clf = SVC(
        kernel="linear",
        probability=True,
        class_weight="balanced"
    )

    try:
        clf.fit(X, y)

    except ValueError:
        return None

    return {
        "classifier": clf,
        "embeddings": X,
        "labels": y
    }


# -------------------------------
# Retrain after New Registration
# -------------------------------
def train_classifier():
    get_trained_model.clear()
    return get_trained_model() is not None


# -------------------------------
# Predict Student Attendance
# -------------------------------
def predict_attendance(image_np):

    encodings = get_face_embeddings(image_np)

    detected_students = {}

    model = get_trained_model()

    if model is None:
        return detected_students, [], len(encodings)

    classifier = model["classifier"]
    embeddings = model["embeddings"]
    labels = model["labels"]

    unique_students = sorted(set(labels))

    for encoding in encodings:

        # Only one student exists
        if len(unique_students) == 1:
            predicted_id = unique_students[0]

        else:
            predicted_id = int(classifier.predict([encoding])[0])

        stored_embedding = embeddings[labels.index(predicted_id)]

        distance = np.linalg.norm(
            stored_embedding - encoding
        )

        THRESHOLD = 0.60

        if distance <= THRESHOLD:
            detected_students[predicted_id] = True

    return detected_students, unique_students, len(encodings)
