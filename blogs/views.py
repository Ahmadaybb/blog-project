from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    posts=Blog.objects.filter(status='Published', category=category_id)
    #try:
    #    category= Category.object.get(pk=category_id)
    #except:
    #    return redirect('home')
    category = get_object_or_404(Category,pk=category_id)
        
    context = {
        'posts' : posts,
        'category': category,
    }
    return render(request,'posts_by_category.html',context)
def blogs(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug,status="Published")
    context={
        'single_blog': single_blog,
    }
    return render(request,'blog.html',context)
def search(request):
    keyword= request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_decription__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request,'search.html',context)