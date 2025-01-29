from pytubefix import YouTube


def download_youtube_video(link):
    yt = YouTube(link, 'WEB')
    print(yt.title)

    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download("data")
    print("Download completed!")


