from django.shortcuts import render
from django.utils.text import slugify
from .models import upload, blog_post, about_post


def mainView(request):


    posts = upload.objects.all().order_by('-upload_time')


    context = {
    "posts" : posts,
    }

    return render(request, 'main.html', context)





def blogView(request):

    posts = blog_post.objects.all().order_by('upload_time')

    context = {
        "posts" : posts,
    }
    return render(request, 'blog.html', context)





def aboutView(request):

    posts = about_post.objects.all()

    context = {
        "posts" : posts,
    }
    return render(request, 'about.html', context)



def detailView(request, slug):
    post = blog_post.objects.get(slug = slug)
    
    context = {
        "post" : post,
    }
    return render(request, 'detail.html', context)