from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.
def articles_list(request):
    articles = models.Articles.objects.all().order_by("date")
    args = {"articles":articles}
    return render(request, 'articles/articleslist.html', args)

def articles_slug(request, slug):
    # return HttpResponse(slug)
    article = models.Articles.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article':article})