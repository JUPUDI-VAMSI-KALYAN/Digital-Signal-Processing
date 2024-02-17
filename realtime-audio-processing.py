import pyaudio
import numpy as np
import scipy.signal

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK_SIZE = 1024
LOW_PASS_FREQ = 1000  # Cutoff frequency for the low-pass filter

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a stream for audio input and output
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)

# Function to apply a simple low-pass filter to the audio data
def low_pass_filter(data, cutoff_freq):
    nyquist_freq = 0.5 * RATE
    normal_cutoff = cutoff_freq / nyquist_freq
    b, a = scipy.signal.butter(5, normal_cutoff, btype='low', analog=False)
    filtered_data = scipy.signal.lfilter(b, a, data)
    return filtered_data

print("Listening...")

# Main loop for real-time audio processing
try:
    while True:
        # Read audio data from the microphone
        audio_data = stream.read(CHUNK_SIZE)
        
        # Convert the audio data to a numpy array for processing
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        
        # Apply the low-pass filter
        processed_data = low_pass_filter(audio_array, LOW_PASS_FREQ)
        
        # Convert the processed data back to bytes
        processed_audio_data = processed_data.astype(np.int16).tobytes()
        
        # Play back the processed audio
        stream.write(processed_audio_data)

except KeyboardInterrupt:
    print("Stopping...")
    stream.stop_stream()
    stream.close()
    audio.terminate()
