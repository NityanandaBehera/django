from django.shortcuts import render
from django.http import HttpResponse

from testapp.models import Employee

def employee_info_view(request):
    employees=Employee.objects.all()
    data={"employees":employees}
    res=render(request,'testapp/employees.html',data)
    return res
def greeting(request):
     s='<h1>hello world</h1>'
     return HttpResponse(s)
    
def contact(request):
    s="<h2> this is my contact page</h2>"
    s+="<h2>contact no:9556846407🥰</h2>"
    return HttpResponse(s)
def home(request):
    msg='hello this is about html page'  
    res= render(request,'testapp/about.html',{'msg':msg})
    return res
    
