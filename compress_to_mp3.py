from pydub import AudioSegment

def compress_audio(input_file, output_file, bitrate='64k'):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="mp3", bitrate=bitrate)

input_file = 'audio.wav'
output_file = 'compressed_audio.mp3'
bitrate = '64k'
compress_audio(input_file, output_file, bitrate)
