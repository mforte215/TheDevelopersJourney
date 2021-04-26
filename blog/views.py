from .models import Blog
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    latest_blog_list = Blog.objects.order_by('-createdAt')[:10]
    return render(request, 'blog/index.html', {'latest_blog_list': latest_blog_list })

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})