from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost, Author, Tag
from django.shortcuts import redirect



def index(request):
    contents = BlogPost.objects.all()
    featured_contents = BlogPost.objects.filter(is_featured=True)

    context = {
        'contents': contents,
        'featured_contents': featured_contents,
    }

    return render(request, 'index.html', context)



def blogpost(request):
    return redirect('/')
