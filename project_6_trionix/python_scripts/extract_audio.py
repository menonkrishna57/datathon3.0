import youtube_downv2 as ytd
import assemblyai as aai

aai.settings.api_key = "ce8209cdfb214d80b63881d941a2b015"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("data/aiml.mp4")

with open("transcript.txt", "w") as file:
    file.write(transcript.text)
