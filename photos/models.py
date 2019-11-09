from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=60)

    def __str__(self):
        return self.location_name


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_desc = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.image_name