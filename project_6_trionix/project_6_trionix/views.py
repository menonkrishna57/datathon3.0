from django.shortcuts import render
from django.http import HttpResponse
import requests
from python_scripts import youtube_downv2
from python_scripts import vector_embedding as ve

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
        youtube_downv2.download_youtube_video(link)
    except:
        pass
    return render(request, 'download.html',{'data': link})

def output(request):
    data=requests.get("https://reqres.in/api/users")
    print(data.text)
    return render(request, 'download.html', {'data': data.text}) 

def transcribe(request):
    myobj=ve
    res=None
    try:
        link=request.GET['linkInput']
        print(link)
        trans_path=youtube_downv2.download_youtube_video(link)
        loaded_sentences,loaded_embeddings,model=myobj.main(trans_path)
        res=myobj.myquery(trans_path,loaded_sentences,loaded_embeddings,model)

    except AttributeError:
        print("oh damn")

    return render(request, 'query.html', {'data': res})

def upload(request):
    global link
    link=request.GET['linkIorm']
    global trans_path
    trans_path=youtube_downv2.download_youtube_video(link)
    transcribe(request)