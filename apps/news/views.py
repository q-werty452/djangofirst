from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils.text import slugify


from apps.news.models import News, Category
from apps.news.forms import CommentForm
from django.db.models import Q 


@login_required
def profile(request):
    user_news = News.objects.filter(author=request.user)
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'user_news':user_news,
        'category_all':category_all
    }
    return render(request, 'pages/profile.html', context)


def registr ( request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request, 'pages/registr.html', context)
        





def search(request):
    category_all = Category.objects.filter(news__isnull=False).distinct()
    query = request.GET.get('q', '')
    results = []
    if query:
        results = News.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    context = {
        'query':query,
        'results':results,
        'category_all':category_all,
    }
    return render(request, 'pages/search.html', context)


def homepage(request):
    news_all = News.objects.all()
    category_all = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'news_all':news_all, 
        'category_all':category_all
    }
    return render(request, 'index.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    category_all = Category.objects.filter(news__isnull=False).distinct()
    comments = news.comments.filter(is_published=True).order_by("-created_at")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news 
            comment.save()
            return redirect('news_detail', slug=slug)
    else:
        form=CommentForm()
    context={
        'news':news,
        'comments':comments,
        'form':form,
        'category_all':category_all
    }
    return render(request,  'pages/single-page.html', context)


def category_detail(request, slug):
    category_all = Category.objects.filter(news__isnull=False).distinct()
    category = get_object_or_404(Category, slug=slug)
    news = News.objects.filter(category=category)
    context = {
        'news':news,
        'category_all':category_all
    }
    return render(request, 'pages/category.html', context)