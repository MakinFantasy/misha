from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail

from base.models import Post, Category, Comment


# Create your views here.
def send(request):
	send_mail(
		"Subject here",
		"Here is the message TEST TEST TEST",
		"beingp0z1t1v3@gmail.com",
		["flammeturk@gmail.com", "tap00k@mail.ru"],
		fail_silently=False,
	)
	return JsonResponse({"message": "EMAIL"})


def index(request):
	post = Post.objects.all().first()
	posts = Post.objects.all()[0:3]
	categories = Category.objects.all()[0:3]

	return render(
		request,
		'index.html',
		{'post': post, 'posts': posts, 'categories': categories,}
	)


def category(request, id):
	category = Category.objects.get(id=id)
	news = Post.objects.filter(category=category)

	return render(
		request,
		'categoryNews.html',
		{
			"news": news,
			"category": category
		}
	)


def categories(request):
	categories = Category.objects.all()

	return render(
		request,
		'categories.html',
		{'categories': categories}
	)


def posts(request):
	news = Post.objects.all()

	return render(
		request,
		'posts.html',
		{'news': news,}
	)


def post_detail_view(request, id):
	post = Post.objects.get(id=id)
	if request.method == 'POST':
		name = request.POST['name']
		comment = request.POST['message']
		email = request.POST['email']
		Comment.objects.create(
			post=post,
			title=name,
			email=email,
			content=comment
		)
		messages.success(request, 'Your comment now in moderation mode.')
	category = Category.objects.get(id=post.category.id)
	comments = Comment.objects.filter(post=post, status=True).order_by('-id')
	related_news = Post.objects.filter(category=category).exclude(id=id)

	return render(
		request,
		'detail.html',
		{
			'news': post,
			'related_news': related_news,
			'comments': comments
		}
	)

