from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    
    page_title = 'CREATE'
    submit_btn_value = '작성완료'
    context = {
        'form': form,
        'page_title': page_title,
        'submit_btn_value': submit_btn_value,
    }
    return render(request, 'community/form.html', context)


@require_safe
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_safe
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'community/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    
    page_title = 'UPDATE'
    submit_btn_value = '수정완료'
    context = {
        'form': form,
        'page_title': page_title,
        'submit_btn_value': submit_btn_value,
    }
    return render(request, 'community/form.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return redirect('community:index')
    
    return redirect('community:detail', pk)