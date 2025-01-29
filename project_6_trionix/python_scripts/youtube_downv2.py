from pytubefix import YouTube
import youtube_downv2 as ytd
import assemblyai as aai
import requests

def download_video(link, output_path):
    response = requests.get(link, stream=True)
    with open(output_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f"Downloaded video to {output_path}")

def transcribe_video(file_path, api_key):
    aai.settings.api_key = api_key
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file_path)
    with open("transcript.txt", "w") as file:
        file.write(transcript.text)
    print("Transcription saved to transcript.txt")
    return transcript.text  # Return the transcription text

def download_youtube_video(link):
    yt = YouTube(link, 'WEB')
    print(yt.title)

    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    video_path = "data/" + yt.title + ".mp4"
    ys.download("data")

    aai.settings.api_key = "ce8209cdfb214d80b63881d941a2b015"
    transcriber = aai.Transcriber()

    # Transcribe the downloaded video file
    print(video_path)
    transcript = transcriber.transcribe(video_path)

    with open("transcript.txt", "w") as file:
        file.write(transcript.text)

    return video_path  # Return the path to the downloaded video file

def get_transcription_from_file():
    try:
        with open("transcript.txt", "r") as file:
            transcription = file.read()
        return transcription
    except FileNotFoundError:
        print("Transcription file not found.")
        return None

# Main function to handle the flow
def main():
    link = "https://www.youtube.com/watch?v=9bZkp7q19f0"
    video_file_path = download_youtube_video(link)
    print(f"Downloaded video file path: {video_file_path}")

    # Get the transcription from the saved file
    transcription = get_transcription_from_file()
    if transcription:
        print("Transcription:")
        print(transcription)

if __name__ == "__main__":
    main()