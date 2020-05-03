from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# args is a dictionary relating to the key world args given the dynamic url
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

def talk_detail_view(request, talk_id, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse(f"<h1>Hello {talk_id}</h1>")