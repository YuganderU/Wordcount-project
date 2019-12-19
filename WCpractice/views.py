from django.http import HttpResponse as hr
from django.shortcuts import render as r 

def homepage(request):
    return r(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()

    wordlist.sort()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    return r(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':worddictionary.items()})

def about(request):
    return r(request,'about.html')