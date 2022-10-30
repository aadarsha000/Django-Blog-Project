from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def postlist(request):
    posts = Post.objects.filter(status="published")
    return render(request, 'index.html', {"posts":posts})

def postdetail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {"post":post})
