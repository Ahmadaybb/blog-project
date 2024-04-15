from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import Blog, Category,Comment

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
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
        
    comments=Comment.objects.filter(blog=single_blog)
    c_count=comments.count()
    context={
        'single_blog': single_blog,
        'comments':comments,
        "c_count" : c_count,
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