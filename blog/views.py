from django.shortcuts import render

# Create your views here.

posts = [
  {'Author':'Chris','Title':'BookA','Content':'Some word here','Date':'August 26 2025'},
  {'Author':'Ruby','Title':'BookB','Content':'Some word here','Date':'August 24 2022'},
  {'Author':'Andy','Title':'BookC','Content':'Some word here','Date':'August 13 2024'},
  {'Author':'Yolanda','Title':'BookD','Content':'Some word here','Date':'August 01 2017'},
]

def home_page(request):
  context = {
    'posts':posts
  }
  return render(request, 'blog/home.html', context)


def about_page(request):
  return render(request,'blog/about.html',{'title':'About'})
