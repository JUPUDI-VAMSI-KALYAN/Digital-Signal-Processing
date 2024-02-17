from pydub import AudioSegment

def convert_mp3_to_wav(input_file, output_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_file)
    
    # Export the audio to WAV format
    audio.export(output_file, format="wav")

# Example usage
input_file = "Ammayi.mp3"
output_file = "audio.wav"
convert_mp3_to_wav(input_file, output_file)
