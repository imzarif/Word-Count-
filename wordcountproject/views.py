from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext=request.GET['full text']
    wordlist=fulltext.split()
    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    wordsorted=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html', {"fulltext":fulltext,"count":len(wordlist),"wordsorted":wordsorted})