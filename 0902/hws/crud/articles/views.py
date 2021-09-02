from django.shortcuts import redirect, render
from .models import Article

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:index')


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    if request.method == 'GET':
        return redirect('articles:detail', pk)
    elif request.method == 'POST':
        article = Article.objects.get(pk=pk)

        context = {
            'article': article,
        }
        return render(request, 'articles/edit.html', context)


def update(request, pk):
    if request.method == 'GET':
        return redirect('articles:detail', pk)
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article.objects.get(pk=pk)
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', pk)


def delete(request, pk):
    if request.method == 'GET':
        return redirect('articles:detail', pk)
    elif request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()

        return redirect('articles:index')