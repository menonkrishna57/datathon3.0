import assemblyai as aai
import os
def main(filelink):    
    aai.settings.api_key = "ce8209cdfb214d80b63881d941a2b015"
    transcriber = aai.Transcriber()
    file_path=os.path.join(os.getcwd(),"data","processed")
    os.makedirs(file_path, exist_ok=True)
    transcript = transcriber.transcribe(filelink)
    filelink=os.path.join(file_path,"transcript.txt")
    with open(filelink, "w") as file:
        file.write(transcript.text)
    return filelink