from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost



def index(request):
    contents = BlogPost.objects.all()

    context = {
        'contents': contents,
    }

    return render(request, 'index.html', context)
