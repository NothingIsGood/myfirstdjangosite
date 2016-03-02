from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Category, Tag, Page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.contrib.auth.models import User

#def post_list(request):
#    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#    return render(request, 'blog/post_list.html', {'posts': posts})

def listing(request):
    contact_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    paginator = Paginator(contact_list, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render_to_response('blog/post_list.html', {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def tag (request, pk): 
    tag = Tag.objects.select_related().get(pk=pk)
    posts = tag.post_set.all()
    return render(request, 'blog/tagpage.html', {'posts': posts, 'tag': tag})

def category(request, pk): 
    category = Category.objects.select_related().get(pk=pk) 
    posts = category.post_set.all() 
    return render(request, 'blog/catpage.html', {'posts': posts, 
                                            'category': category})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'blog/page_detail.html', {'page' : page})

def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'base.html', {'categories' : categories})