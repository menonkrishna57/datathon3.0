from django.shortcuts import render
from django.http import HttpResponse
import requests
from python_scripts import youtube_downv3
from python_scripts import all_con as ac

def home(request):
    return render(request, 'youtube_trans.html')


def login(request):
    return render(request, 'login/login.html')

def signup(request):
    return render(request, 'login/register_acc.html')

def download(request):
    link=None

    try:
        link=request.GET['linkInput']
        youtube_downv3.download_youtube_video(link)
    except:
        pass
    return render(request, 'download.html',{'data': link})

def output(request):
    data=requests.get("https://reqres.in/api/users")
    print(data.text)
    return render(request, 'download.html', {'data': data.text}) 

def transcribev1(request):
    myobj=ve
    res=None
    try:
        link=request.GET['linkInput']
        print(link)
        trans_path=youtube_downv3.download_youtube_video(link)
        loaded_sentences,loaded_embeddings,model=myobj.main(trans_path)
        res=myobj.myquery(trans_path,loaded_sentences,loaded_embeddings,model)

    except AttributeError:
        print("oh damn")

    return render(request, 'query.html', {'data': res})

def transcribe(request):
    render(request, 'loader.html')
    try:
        # global loaded_sentences,loaded_embeddings,model
        user_query=request.GET['linkInput']
        loaded_sentences,loaded_embeddings,model=ac.main(user_query)
    except AttributeError:
        print("oh damn")

def query(request):
    user_query=request.GET['myquery']
    res=ac.myquery(user_query)
    return render(request, 'query.html',{'data': res})

def upload(request):
    global link
    link=request.GET['linkIorm']
    global trans_path
    trans_path=youtube_downv3.download_youtube_video(link)
    transcribe(request)

def ytdownload(request):
    return render(request, 'youtube_downloader.html')
def audio(request):
    return render(request, 'audio_down.html')
def loading(request):
    return render(request, 'loader.html')