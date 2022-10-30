from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.utils.text import slugify

# Create your views here.
def postlist(request):
    posts = Post.objects.filter(status="published")
    return render(request, 'blog\index.html', {"posts":posts})

def postdetail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog\detail.html', {"post":post})

def postCreate(request):
    context={}
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = request.user
            post.slug = slugify(post.title)
            post.author = user
            post.save()
            return redirect("blog:home")
        else:
            form = PostForm()
    else:
        form = PostForm()
        context['form']=form
    return render(request, 'blog/create.html', context )
