from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def result(request):
    que='who is the father of py'
    a='Nitya'
    b='Abhisek'
    c='Piyush'
    d='Succhak'
    level='Easy'
    data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res