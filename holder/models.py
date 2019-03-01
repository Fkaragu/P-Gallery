from django.db import models

class Image(models.Model):
   name = models.CharField(max_length =60)
   description = models.TextField()
   location = models.ForeignKey(Location)
   category = models.ForeignKey(Category)
   pub_date = models.DateTimeField(auto_now_add=True)
   article_image = models.ImageField(upload_to = 'articles/')

class Location(models.Model):
  name = models.CharField(max_length =60)

class Category(models.Model):
   name = models.CharField(max_length =60)
