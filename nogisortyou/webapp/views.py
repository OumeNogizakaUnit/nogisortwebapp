from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request, 'base.html')

def login_view(request):
    return HttpResponse('ここはログインページ')

def test_view(request):
    return render(request, 'unko.html')
