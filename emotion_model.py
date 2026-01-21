import librosa
import numpy as np

def predict_emotion(file_path):
    y, sr = librosa.load(file_path)

    energy = np.mean(librosa.feature.rms(y=y))
    pitch = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))

    if energy < 0.02:
        return "Sad 😢"
    elif pitch > 3000:
        return "Angry 😠"
    elif energy > 0.05:
        return "Happy 😊"
    else:
        return "Neutral 😐"
