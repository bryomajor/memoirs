from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def my_photos(request):
    photos = Image.show_all_photos()
    # category_results = category.objects.all()
    return render(request, 'all-photos/photos.html', {"photos":photos,})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Image.search_photo_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html', {"message":message, "photos":searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message":message})


def get_category(request, category):
    category_results = category.objects.all()
    location_results = Location.objects.all()
    category_result = Image.objects.filter(category__category_name = category)
    return render(request,'all-photos/photos.html',{'all_images':category_result,'category_results':category_results,'location_results':location_results})

def get_location(request):
    category_results = category.objects.all()
    location_results = Location.objects.all()
    location_result = Image.objects.filter(location__location_name= location)
    return render(request,'all-photos/photos.html',{'all_images':location_result,'category_results':category_results,'location_results':location_results})