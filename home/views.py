from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post, Word

def index(request):
    posts = Post.objects.order_by('-date_posted')
    return render(request, "home/index.html", context={"posts": posts})

def test(request):
    words = Word.objects.order_by('-word')
    return render(request, "home/test.html", context={"words": words})
