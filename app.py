import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load Model
model = tf.keras.models.load_model("Pneumonia_Detection_EfficientNetB0.keras")

CLASS_NAMES = ["NORMAL", "PNEUMONIA"]

st.set_page_config(page_title="Pneumonia Detection", layout="centered")

st.title("🫁 Pneumonia Detection")
st.write("Upload a Chest X-ray image to predict whether it is NORMAL or PNEUMONIA.")

uploaded_file = st.file_uploader(
    "Choose an X-ray image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    image = image.resize((224, 224))

    img_array = np.array(image, dtype=np.float32)

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)[0][0]

    confidence = prediction if prediction >= 0.5 else 1 - prediction

    predicted_class = CLASS_NAMES[int(prediction >= 0.5)]

    st.subheader(f"Prediction: {predicted_class}")

    st.write(f"Confidence: **{confidence*100:.2f}%**")
