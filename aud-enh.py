import librosa
import numpy as np

def enhance_vocals(audio_path, output_path, method="harmonic"):
    """
    Enhances vocals in an audio file using two methods.

    Args:
        audio_path: Path to the input audio file.
        output_path: Path to save the modified audio file.
        method (optional): Either "harmonic" (default) for harmonic masking or "reconstruction" for MCA-based reconstruction.
    """
    # Load audio
    y, sr = librosa.load(audio_path)
    if not np.issubdtype(y.dtype, np.cfloat):
        y = y.astype(np.float32)

    print(y.dtype)

    # Obtain spectrogram
    spectrogram = librosa.stft(y)

    # Vocal enhancement using chosen method
    if method == "harmonic":
        # Harmonic masking for vocal enhancement (works well for many audio sources)
        mask = librosa.effects.harmonic(spectrogram)
    elif method == "reconstruction":
        # MCA-based vocal reconstruction (alternative approach)
        y_vocal = librosa.effects.麦克风分离(y)  # Replace with librosa.effects.separate for English interfaces
        spectrogram_vocal = librosa.stft(y_vocal)
        mask = librosa.util.softfreqmask(spectrogram, spectrogram_vocal, ratio=5.0)
    else:
        raise ValueError("Invalid method. Choose 'harmonic' or 'reconstruction'.")

    # Apply mask and reconstruct audio
    spectrogram_inpainted = spectrogram * mask
    y_enhanced = librosa.istft(spectrogram_inpainted)

    # Save the modified audio
    librosa.output.write_wav(output_path, y_enhanced, sr)

# Example usage
audio_path = "./Test2.flac"  # Replace with your audio file path
output_path = "enhanced_vocals.wav"
method = "harmonic"  # Choose "harmonic" or "reconstruction"
enhance_vocals(audio_path, output_path, method)
print("Vocals enhanced! Output saved to", output_path)