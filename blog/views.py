from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from blog.forms import userForm, CommentForm
from django.template import RequestContext
from datetime import datetime
import logging
# Create your views here.
def index(request):
    context = {
        'title' : 'Portfolio',
    }
    return render(request, 'blog/index.html', context=context)

def blog_posts(request):
    all_post = Post.objects.all()
    paginator = Paginator(all_post, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'title' : 'Portfolio',
        'posts' : posts
    }
    return render(request, 'blog/post_list.html', context=context)

@login_required(login_url='/login/')
def post_detail(request, id):
    p_id = id
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.POST['name']
            comment.comment = request.POST['comment']
            comment.post_id = id
            comment.save()
    else:
        form = CommentForm

    context = {
        'post':  get_object_or_404(Post, id=id),
        'comment': Comment.objects.filter(post_id=id),
        'title': 'Blog',
        'p_id': p_id,
        'form': form
    }
    if request.user.is_authenticated:
        return render(request, 'blog/post_detail.html', context=context)




logger = logging.getLogger(__name__)

def faq(request):
    return render(request, 'blog/faq.html')

def about(request):
    return render(request, 'blog/about.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'blog/login_success.html')
        else:
            return render(request, 'blog/access_denied.html')

    return render(request, 'blog/login.html')

def singup(request,id):
    if request.method=='POST':
        form = userForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            return render(request, 'blog/singup_success.html')
    else:
        form = userForm()
    return render(request,'blog/singup.html', {'form': form})



# HTTP Error 400
def bad_request(request):
    response = render_to_response(
        '404.html',context_instance=RequestContext(request)
        )
    response.status_code = 404
    return response

