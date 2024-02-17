import numpy as np
import scipy.io.wavfile as wavfile

def compress_audio(input_file, output_file, bits_per_sample):
    # Read the input audio file
    sample_rate, audio_data = wavfile.read(input_file)
    
    # Normalize the audio data to the range [-1, 1]
    max_val = np.max(np.abs(audio_data))
    audio_data = audio_data.astype(np.float32) / max_val
    
    # Calculate the quantization step size based on the number of bits per sample
    quantization_step = 2.0 / (2 ** bits_per_sample)
    
    # Apply uniform quantization to the audio data
    quantized_audio_data = np.round(audio_data / quantization_step) * quantization_step
    
    # Scale the quantized audio data back to the original range
    quantized_audio_data *= max_val
    
    # Convert the quantized audio data back to the original data type
    quantized_audio_data = quantized_audio_data.astype(np.int16)
    
    # Write the compressed audio data to a new file
    wavfile.write(output_file, sample_rate, quantized_audio_data)

# Example usage: compress the input audio file using 4 bits per sample
input_file = 'audio.wav'
output_file = 'compressed_audio.wav'
bits_per_sample = 4
compress_audio(input_file, output_file, bits_per_sample)
