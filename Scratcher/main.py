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

    # Generate crackling effect
    crackle = np.random.normal(0, 0.002, noise_len)
    crackle[np.abs(crackle) < 0.001] = 0
    
    # Generate low-frequency rumble
    t = np.linspace(0, noise_len/sr, noise_len, endpoint=False)
    rumble = 0.002 * np.sin(2 * np.pi * 5 * t)

    # Combine effects
    vinyl_effect = vinyl_noise + crackle + rumble
    
    # Add vinyl effect to the original audio
    y_vinyl = y + vinyl_effect
    
    


input_file = "./Test/Test1.wav"
output_file = "./Test/scratched.wav"

add_vinyl_effect(input_file, output_file)