from django.shortcuts import render
from .models import upload, blog_post


def mainView(request):


    posts = upload.objects.all().order_by('-upload_time')


    context = {
    "posts" : posts,
    }

    return render(request, 'main.html', context)





def blogView(request):

    posts = blog_post.objects.all().order_by('-upload_time')

    context = {
        "posts" : posts,
    }
    return render(request, 'blog.html', context)





def aboutView(request):



    context = {

    }
    return render(request, 'about.html', context)

