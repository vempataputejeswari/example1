from django.db import models

# Create your models here.

class category(models.Model):

	name = models.CharField('categories',max_length=30)
	
	def __str__ (self):
	   return self.name

class book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	page = models.IntegerField(default=0)
	summary = models.TextField()
	category = models.ManyToManyField(category,related_name='book')
	pdf = models.FileField(upload_to = 'pdf')
	recommanded_books = models.BooleanField(default=False)
	bussiness_books = models.BooleanField(default=False)
	fiction_books = models.BooleanField(default=False)
	def __str__(self):
	   return self.title
class Meta:
	db_table = "book"

	