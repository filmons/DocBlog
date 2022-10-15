
from django.urls import path
from .views import index, article

urlpatterns = [
    path("", index, name="blog-homepage"),
    path("article_<str:numero_article>/", article, name="blog-article")
]