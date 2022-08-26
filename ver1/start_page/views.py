from django.shortcuts import render
from django.http import HttpResponse


def start_page(request):
    return HttpResponse('''<h1>Start page</h1>
    <a href='http://127.0.0.1:8000/news/'>News</a> ''')
# Create your views here.
