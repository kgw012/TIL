from django.shortcuts import render

def dinner(request, menu, p_num):
    context = {
        'menu': menu,
        'p_num': p_num,
    }
    return render(request, 'dinner.html', context)