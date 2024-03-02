from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta
from .models import *
from .forms import *

def home(request):
    context = {}
    return render(request, 'app/index.html', context)

def detail(request, id):
    context = {}
    return render(request, 'app/detail.html', context)

@login_required
def create(request):
    context = {}
    if request.method == 'GET':
        form = RecipeForm()
        context['form'] = RecipeForm()
        return render(request, 'app/create.html', context)
    elif request.method == 'POST' and request.FILES != None:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new = Recipe()
            user = request.user
            new.name = form['name'].value()
            new.ingredients = form['ingredients'].value()
            new.prep = form['prep'].value()
            new.cook = form['serving'].value()
            new.ingredients = form['ingredients'].value()
            new.directions = form['directions'].value()
            new.notes = form['notes'].value()
            theimg = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(theimg.name, theimg)
            file_url = fs.url(filename)
            new.image = filename
            new.save()
            return redirect('home')
        else:
            form = RecipeForm()
            context['form'] = RecipeForm()
            return render(request, 'app/create.html', context)
    return render(request, 'app/create.html', context)

def update(request, id):
    context = {}
    return render(request, 'app/update.html', context)

def delete(request, id):
    context = {}
    return render(request, 'app/delete.html', context)