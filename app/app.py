"""
Real-Time Image Classification Web App
======================================

This Flask application provides a web interface for real-time image classification
using a trained CIFAR-10 model. It captures video from your webcam and classifies
each frame into one of 10 categories.

Usage:
    python app.py

Then open your browser to http://localhost:5000
"""

from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
import base64

# Initialize Flask app
app = Flask(__name__)

# CIFAR-10 class names
CLASS_NAMES = [
    'Airplane ✈️', 'Automobile 🚗', 'Bird 🐦', 'Cat 🐱', 'Deer 🦌',
    'Dog 🐕', 'Frog 🐸', 'Horse 🐴', 'Ship 🚢', 'Truck 🚚'
]

# Global variables
model = None
camera = None

def load_model():
    """
    Load the trained CIFAR-10 model.

    Returns:
        Loaded Keras model or None if model file doesn't exist
    """
    global model

    model_path = os.path.join('models', 'cifar10_model.h5')

    # Check if model exists
    if not os.path.exists(model_path):
        print(f"⚠️  Model not found at {model_path}")
        print("Please train the model first using notebooks/01_train_model.ipynb")
        return None

    try:
        model = keras.models.load_model(model_path)
        print(f"✅ Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None


def preprocess_frame(frame):
    """
    Preprocess a video frame for model prediction.

    Args:
        frame: OpenCV image (BGR format)

    Returns:
        Preprocessed image ready for model input (1, 32, 32, 3)
    """
    # Resize to 32x32 (CIFAR-10 input size)
    resized = cv2.resize(frame, (32, 32))

    # Convert BGR to RGB
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

    # Normalize to [0, 1]
    normalized = rgb.astype('float32') / 255.0

    # Add batch dimension
    batched = np.expand_dims(normalized, axis=0)

    return batched


def predict_frame(frame):
    """
    Make a prediction on a video frame.

    Args:
        frame: OpenCV image

    Returns:
        tuple: (predicted_class_name, confidence_percentage)
    """
    if model is None:
        return "No Model", 0.0

    # Preprocess the frame
    processed = preprocess_frame(frame)

    # Make prediction
    predictions = model.predict(processed, verbose=0)

    # Get the predicted class and confidence
    predicted_idx = np.argmax(predictions[0])
    confidence = predictions[0][predicted_idx] * 100

    return CLASS_NAMES[predicted_idx], confidence


def generate_frames():
    """
    Generator function that yields video frames with predictions.

    Yields:
        JPEG-encoded frames with prediction overlays
    """
    global camera

    # Initialize camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("❌ Error: Could not open webcam")
        return

    print("📹 Webcam opened successfully")

    try:
        while True:
            success, frame = camera.read()

            if not success:
                break

            # Make prediction
            predicted_class, confidence = predict_frame(frame)

            # Add prediction text to frame
            # Background rectangle for better text visibility
            cv2.rectangle(frame, (10, 10), (400, 100), (0, 0, 0), -1)

            # Prediction text
            text = f"{predicted_class}"
            confidence_text = f"Confidence: {confidence:.2f}%"

            # Color based on confidence
            if confidence > 70:
                color = (0, 255, 0)  # Green
            elif confidence > 40:
                color = (0, 255, 255)  # Yellow
            else:
                color = (0, 0, 255)  # Red

            cv2.putText(frame, text, (20, 45),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            cv2.putText(frame, confidence_text, (20, 75),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Yield frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    finally:
        # Release camera when done
        if camera is not None:
            camera.release()
            print("📹 Webcam released")


@app.route('/')
def index():
    """
    Render the main page.
    """
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    """
    Video streaming route. Returns a multipart response with MJPEG stream.
    """
    return Response(generate_frames(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/model_status')
def model_status():
    """
    Check if model is loaded.

    Returns:
        JSON with model status
    """
    return jsonify({
        'model_loaded': model is not None,
        'classes': CLASS_NAMES
    })


@app.route('/health')
def health():
    """
    Health check endpoint.
    """
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    print("=" * 50)
    print("🎥 Real-Time Image Classification App")
    print("=" * 50)

    # Load the model
    if load_model() is None:
        print("\n⚠️  WARNING: Running without a model!")
        print("Train a model first using: notebooks/01_train_model.ipynb\n")

    print("\n🚀 Starting Flask server...")
    print("📱 Open your browser to: http://localhost:5000")
    print("\n💡 Tip: Use ngrok to share your app publicly!")
    print("   Run: ngrok http 5000")
    print("\nPress CTRL+C to stop\n")

    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
