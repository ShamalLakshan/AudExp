import librosa
import numpy as np
import soundfile as sf

def enhance_vocals(audio_path, output_path, method="harmonic"):
    """
    Enhances vocals in an audio file using two methods.
    Args:
        audio_path: Path to the input audio file.
        output_path: Path to save the modified audio file.
        method (optional): Either "harmonic" (default) for harmonic masking or "reconstruction" for MCA-based reconstruction.
    """
    # Load audio
    y, sr = librosa.load(audio_path, dtype=np.float32)
    
    # Vocal enhancement using chosen method
    if method == "harmonic":
        # Harmonic masking for vocal enhancement
        y_harmonic = librosa.effects.harmonic(y)
        mask = np.abs(librosa.stft(y_harmonic)) / np.abs(librosa.stft(y) + 1e-16)
    elif method == "reconstruction":
        # MCA-based vocal reconstruction (alternative approach)
        y_vocal = librosa.effects.mx.separate(y)  # Using mx.separate instead of 麦克风分离
        mask = np.abs(librosa.stft(y_vocal)) / (np.abs(librosa.stft(y)) + 1e-16)
    else:
        raise ValueError("Invalid method. Choose 'harmonic' or 'reconstruction'.")
    
    # Apply mask and reconstruct audio
    stft = librosa.stft(y)
    stft_enhanced = stft * mask
    y_enhanced = librosa.istft(stft_enhanced)
    
    # Save the modified audio
    sf.write(output_path, y_enhanced, sr)

# Example usage
audio_path = "./Test2.flac"  # Replace with your audio file path
output_path = "enhanced_vocals.wav"
method = "harmonic"  # Choose "harmonic" or "reconstruction"
enhance_vocals(audio_path, output_path, method)
print("Vocals enhanced! Output saved to", output_path)