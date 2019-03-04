from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def post_view(request):
    img = Image.all_images()
    return render(request, 'post.html',{"img":img})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
