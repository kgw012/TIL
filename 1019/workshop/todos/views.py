from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required

@login_required
@require_safe
def index(request):
    context = {

    }
    return render(request, 'todos/index.html', context)