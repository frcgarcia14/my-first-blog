from django.http import HttpResponse
from django.shortcuts import render

def signup(request):
    return render(request,"sign_up.html")
