from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        # 'articles': articles,
        'page_obj': page_obj,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(request, f'{ article.pk }번째 글이 등록되었습니다.')
            return redirect('articles:index')
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            messages.success(request, f'{ article.pk }번째 글이 수정되었습니다.', extra_tags='primary')
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)


def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        messages.error(request, f'{ pk }번째 글이 삭제되었습니다.')
        return redirect('articles:index')

    return redirect('articles:detail', pk)