import librosa
import soundfile as sf
import numpy as np
import wave
import matplotlib.pyplot as plt


def add_vinyl_effect(input_file, output_file):
    # Load the audio file
    y, sr = librosa.load(input_file, sr=None)
    
    # Generate vinyl noise
    noise_len = len(y)
    vinyl_noise = np.random.normal(0, 0.005, noise_len)


input_file = ""
output_file = ""

add_vinyl_effect(input_file, output_file)