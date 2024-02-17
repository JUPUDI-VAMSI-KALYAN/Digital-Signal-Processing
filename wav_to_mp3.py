from pydub import AudioSegment

def convert_wav_to_mp3(input_file, output_file, bitrate='192k'):
    # Load the WAV file
    audio = AudioSegment.from_wav(input_file)
    
    # Export the audio to MP3 format
    audio.export(output_file, format="mp3", bitrate=bitrate)

# Example usage
input_file = "input_audio.wav"
output_file = "output_audio.mp3"
convert_wav_to_mp3(input_file, output_file)
