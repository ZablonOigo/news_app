from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
    newsapi = NewsApiClient(api_key='c4b79d0200624596a1f77441971abfa5')
    top = newsapi.get_top_headlines(sources ='techcrunch')
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
    context={'mylist':mylist}
    return render(request,'newsapp/base.html', context)
# Create your views here.
