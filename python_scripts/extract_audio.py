from moviepy import VideoFileClip
def extract_video(video_path,output):
    video=VideoFileClip(video_path)
    audio=video.audio
    audio.write_audiofile(output)



if __name__=="__main__":
    video_path="aiml.mp4"
    output="audio.mp3"


    extract_video(video_path,output)