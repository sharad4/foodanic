from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'app/index.html', context)

def detail(request, id):
    context = {}
    return render(request, 'app/detail.html', context)

def create(request, id):
    context = {}
    return render(request, 'app/create.html', context)

def update(request, id):
    context = {}
    return render(request, 'app/update.html', context)

def delete(request, id):
    context = {}
    return render(request, 'app/delete.html', context)