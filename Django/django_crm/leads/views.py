from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse('Hello world')
    context = {
        'name': 'Joe',
        'age': 35
    }
    return render(request, 'second_page.html', context)
