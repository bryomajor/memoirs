from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_photos(request):
    return render(request, 'all-photos/photos.html')