from django.db import models
from django.utils import timezone

class Page(models.Model):
	"""Модель для страниц (для меню блога)"""
	title = models.CharField(max_length=255)
	text = models.TextField()

	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Post(models.Model):
	"""Модель для поста Блога"""
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=255)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)

	tag = models.ManyToManyField(Tag, blank = True, null = True)
	category = models.ForeignKey(Category, blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.title
