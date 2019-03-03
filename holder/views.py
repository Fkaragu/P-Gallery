from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def post_view(request):
    img = Image.all_images()
    return render(request, 'post.html',{"img":img})
