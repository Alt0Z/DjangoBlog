from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myblog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post})

def about_page(request):
    about = get_object_or_404
    return render(request, 'myblog/about.html', {'about': about})

def contacts(request):
    contact = get_object_or_404
    return render(request, 'myblog/contacts.html', {'contact': contact})