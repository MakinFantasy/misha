from django.db import models
from django.utils import timezone


class Category(models.Model):
	title = models.CharField(max_length=100)
	date_created = models.DateTimeField(timezone.now())
	image = models.ImageField(upload_to='images/')

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.title


class Tag(models.Model):
	title = models.CharField(max_length=100)
	date_created = models.DateTimeField(timezone.now())

	class Meta:
		verbose_name_plural = "Tags"

	def __str__(self):
		return self.title


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(upload_to='images/')
	date_created = models.DateTimeField(timezone.now())
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)

	class Meta:
		verbose_name_plural = "Posts"

	def __str__(self):
		return self.title


class Comment(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	email = models.EmailField(max_length=254)
	status = models.BooleanField(default=False)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Comments"

	def __str__(self):
		return self.title
