from django.db import models

class Location(models.Model):
  name = models.CharField(max_length =60)

  def __str__(self):
      return self.name

  def save_location(self):
      self.save()

  def update_location(self):
      self.update()

  def delete_location(self):
      self.delete()

class Category(models.Model):
   name = models.CharField(max_length =60)

   def __str__(self):
       return self.name

   def save_category(self):
       self.save()

   def update_category(self):
       self.update()

   def delete_category(self):
       self.delete()

class Image(models.Model):
   name = models.CharField(max_length =60)
   description = models.TextField()
   location = models.ForeignKey(Location)
   category = models.ForeignKey(Category)
   pub_date = models.DateTimeField(auto_now_add=True)
   article_image = models.ImageField(upload_to = 'articles/')

   def __str__(self):
       return self.name

   def save_image(self):
       self.save()

   def update_image(self):
       self.update()

   def delete_image(self):
       self.delete()

   @classmethod
   def all_images(cls):
       img = cls.objects.all()
       return img

   @classmethod
   def get_image_by_id(cls,id):
       img = cls.objects.filter(id__id = id)
       return img

   @classmethod
   def search_by_image(cls,search_cat):
       img = cls.objects.filter(article_image__icontains=search_cat)
       return img

   @classmethod
   def filter_by_location(cls,id):
       img = cls.objects.filter(location__location = id)
       return img
