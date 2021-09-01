from django.shortcuts import render
from datetime import datetime


def homework1(request):
    menus = ['볶음밥', '김치찌개']

    context = {
        'menus': menus,
    }
    return render(request, 'homework1.html', context)


def homework2(request):
    posts = ['포스트1', '포스트2']

    context = {
        'posts': posts,
    }
    return render(request, 'homework2.html', context)


def homework3(request):
    users = []

    context = {
        'users': users,
    }
    return render(request, 'homework3.html', context)


def homework4(request):
    posts = ['포스트1', '포스트2', '포스트3']

    context = {
        'posts': posts,
    }
    return render(request, 'homework4.html', context)


def homework5(request):
    return render(request, 'homework5.html')


def homework6(request):
    today = datetime(2020, 2, 2, 14, 2, 0)

    context = {
        'today': today,
    }
    return render(request, 'homework6.html', context)
