from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from emotion_model import predict_emotion

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "../recordings"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/analyze", methods=["POST"])
def analyze():
    audio = request.files["audio"]
    file_path = os.path.join(UPLOAD_FOLDER, "audio.wav")
    audio.save(file_path)

    emotion = predict_emotion(file_path)
    return jsonify({"emotion": emotion})

if __name__ == "__main__":
    app.run(debug=True)
