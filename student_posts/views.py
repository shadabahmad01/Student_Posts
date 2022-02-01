from django.shortcuts import render,redirect
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Post,Exp
from .forms import PostForm,ExpForm

# Create your views here.

def index(request):
	"""The Home page for learning log."""
	return render(request, 'student_posts/index.html')

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'student_posts/post_detail.html'

def PostList(request):
	object_list = Post.objects.filter(status=1).order_by('-created_on')
	paginator = Paginator(object_list, 3)
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.page(paginator.num_pages)
	return render(request,'student_posts/postlist.html',{'page':page,'post_list':post_list})

@login_required
def new_post(request):
	"""add new post"""
	if request.method != 'POST':
		#no data submitted; create a blank post
		form = PostForm()

	else:
		#post data submitted
		form = PostForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			return redirect('student_posts:home')

	context = {'form': form}
	return render(request,'student_posts/new_post.html',context)

@login_required
def user_post(request):
	"""Show all post of logged in user"""
	object_list = Post.objects.filter(author=request.user).order_by('-created_on')
	paginator = Paginator(object_list, 3)
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.page(paginator.num_pages)

	return render(request,'student_posts/user_post.html',{'page':page,'post_list':post_list})

class ExpDetail(generic.DetailView):
	model = Exp
	template_name = 'student_posts/expdetail.html'

def ExpList(request):
	object_list = Exp.objects.filter(status=1).order_by('-created_on')
	paginator = Paginator(object_list, 3)
	page = request.GET.get('page')
	try:
		exp_list = paginator.page(page)
	except PageNotAnInteger:
		exp_list = paginator.page(1)
	except EmptyPage:
		exp_list = paginator.page(paginator.num_pages)

	return render(request,'student_posts/explist.html',{'page':page,'exp_list':exp_list})

@login_required
def new_exp(request):
	"""add new interview experience"""
	if request.method != 'POST':
		#no data submitted; create a blank post
		form = ExpForm()

	else:
		#post data submitted
		form = ExpForm(data=request.POST)
		if form.is_valid():
			new_exp = form.save(commit=False)
			new_exp.author = request.user
			new_exp.save()
			return redirect('student_posts:home')

	context = {'form': form}
	return render(request,'student_posts/new_exp.html',context)

@login_required
def user_exp(request):
	"""Show all post of logged in user"""
	object_list = Exp.objects.filter(author=request.user).order_by('-created_on')
	paginator = Paginator(object_list, 3)
	page = request.GET.get('page')
	try:
		exp_list = paginator.page(page)
	except PageNotAnInteger:
		exp_list = paginator.page(1)
	except EmptyPage:
		exp_list = paginator.page(paginator.num_pages)

	return render(request,'student_posts/user_exp.html',{'page':page,'exp_list':exp_list})
