from django.test import TestCase
from .models import Image,Location,Category


class Image_TestCases(TestCase):
    def setUp(self):
        self.new_location = Location(name = 'Kenya')
        self.new_location.save_location()
        self.new_category = Category(name='Travel')
        self.new_category.save_category()

        self.new_image = Image(id=1,name='test', description='Loprem',article_image='media/articles/Nature.jpg',category=self.new_category,location=self.new_location)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save_method(self):
        self.new_image.save_image()
        all_obj = Image.objects.all()
        self.assertTrue(len(all_obj)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        obj_filt = Image.objects.filter(name='test')
        Image.delete_image(obj_filt)
        obj_all = Image.objects.all()
        self.assertTrue(len(obj_all) == 0)

    
