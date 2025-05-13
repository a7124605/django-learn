from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="blog_home_page"),
    path("about/", views.about_page, name="blog_about_page"),
]
