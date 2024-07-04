# Vinyl Effect Audio Processor

This Python script adds vinyl record effects to an audio file, simulating the sound of an old vinyl recording. It uses various audio processing techniques to achieve this effect.

## Features

1. **Vinyl Noise Generation**: Adds a layer of background noise typical of vinyl playback.
2. **Crackling Effect**: Simulates the pops and crackles often heard on vinyl records.
3. **Low-Frequency Rumble**: Adds a subtle low-frequency oscillation to mimic turntable rumble.
4. **Frequency Response Simulation**: Applies a low-pass filter to replicate the limited high-frequency response of vinyl playback systems.
5. **Waveform Visualization**: Generates plots comparing the original and processed audio waveforms.

## How It Works

1. **Audio Loading**: The input audio file is loaded using the librosa library.

2. **Vinyl Noise**: Random Gaussian noise is generated and added to the audio to simulate the characteristic hiss of vinyl playback.

3. **Crackling Effect**: Another layer of Gaussian noise is created, but with a threshold applied to create intermittent crackles.

4. **Low-Frequency Rumble**: A low-frequency sine wave is generated to simulate the subtle rumble of a turntable.

5. **Effect Combination**: The noise, crackles, and rumble are combined and added to the original audio.

6. **Frequency Response Simulation**: A low-pass filter is applied to the audio, cutting off frequencies above 10 kHz. This simulates the limited high-frequency response of vinyl records and playback systems.

7. **Audio Normalization**: The processed audio is normalized to prevent clipping and ensure a consistent volume level.

8. **Output**: The modified audio is saved to a new file.

9. **Visualization**: Matplotlib is used to create waveform plots of both the original and processed audio for comparison.

## Usage

1. Ensure all required libraries are installed (librosa, soundfile, numpy, wave, matplotlib).
2. Set the `input_file` variable to the path of your audio file.
3. Set the `output_file` variable to your desired output path.
4. Run the script.

The script will process the audio and save the result to the specified output file. It will also display a plot comparing the original and processed audio waveforms.

## Customization

You can adjust the intensity of the effects by modifying the parameters in the `add_vinyl_effect` function:
- Change the standard deviation in the `np.random.normal()` calls to adjust the intensity of the noise and crackles.
- Modify the amplitude and frequency of the sine wave in the rumble generation to alter the low-frequency effect.
- Adjust the cutoff frequency in the `librosa.effects.low_pass_filter()` call to change the high-frequency roll-off point.