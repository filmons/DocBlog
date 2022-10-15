from django.shortcuts import render
from datetime import datetime


def vue_de_test(request):
    return render(request, "DocBlog/index.html", context={"date": datetime.today()})
