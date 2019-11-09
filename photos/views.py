from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def my_photos(request):
    photos = Image.show_all_photos()
    return render(request, 'all-photos/photos.html', {"photos":photos})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Image.search_photo_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html', {"message":message, "photos":searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message":message})