from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.filter(status='P')
    return render(request, 'blog/index.html',context={'posts':posts})

# Create your views here.
def post_details(request,id):
    try:
        posts = Post.objects.filter(id=id)
        return render(request, 'blog/test.html',context={'posts':posts})
    except:
        return HttpResponse("The page you're looking doesn't exsist")