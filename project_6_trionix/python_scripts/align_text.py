import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
import numpy as np

# Load the video and audio
video = mp.VideoFileClip('your_video.mp4')
audio = video.audio

# Save the audio to a temporary file (required by speech_recognition)
audio.write_audiofile('temp_audio.wav')

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the transcribed audio
with sr.AudioFile('temp_audio.wav') as source:
    audio_data = recognizer.record(source)

# Transcribe the audio
transcription = recognizer.recognize_google(audio_data)

# Now you have the transcription, you need to align it with the video frames
# This is a simplified example and may require more sophisticated methods for accurate alignment

# Get the duration of each frame in milliseconds (assuming 30 fps)
frame_duration = int(1000 / video.fps)

# Create a list to store aligned timestamps
aligned_timestamps = []

# Assume transcription is in a single line for simplicity
transcription_lines = transcription.split('\n')

for i, line in enumerate(transcription_lines):
    # For each transcribed segment, find the corresponding video frame
    # This is a simplified approach and may need adjustments based on actual data
    start_time = i * frame_duration  # Approximate start time of the frame
    end_time = (i + 1) * frame_duration  # Approximate end time of the frame
    aligned_timestamps.append((start_time, end_time))

# Now you have aligned timestamps corresponding to each video frame
print(aligned_timestamps)