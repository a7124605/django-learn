from django.shortcuts import render

from .models import Post

# Create your views here.

posts = [
    {
        "author": "Chris",
        "title": "BookA",
        "content": "Some word here",
        "date_posted": "August 26 2025",
    },
    {
        "author": "Ruby",
        "title": "BookB",
        "content": "Some word here",
        "date_posted": "August 24 2022",
    },
    {
        "author": "Andy",
        "title": "BookC",
        "content": "Some word here",
        "date_posted": "August 13 2024",
    },
    {
        "author": "Yolanda",
        "title": "BookD",
        "content": "Some word here",
        "date_posted": "August 01 2017",
    },
]


def home_page(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about_page(request):
    return render(request, "blog/about.html", {"title": "About"})
