# Create your views here.
from datetime import datetime

from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html", context={"date": datetime.today()})


def article(request, numero_article):
    if numero_article in ["01", "02" , "03"]:
        return render(request, f"blog/article_{numero_article}.html")
    return render(request, 'blog/article_not_found.html')
