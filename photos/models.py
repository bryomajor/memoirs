from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=60)

    def __str__(self):
        return self.location_name


class category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_desc = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(category)
    photo = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.image_name