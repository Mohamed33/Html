from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
def article_list(req):
    articles = Articles.objects.all().order_by('date')
    return render(req,'articels/articels.html',{'articels' : articles})

def article_details(req,slug):
    article = Articles.objects.get(slug=slug)
    return render(req ,'articels/article_details.html',{'article':article})

    #return render(req,'articels/article_details.html')
# Create your views here.
