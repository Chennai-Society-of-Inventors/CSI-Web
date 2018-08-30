from django.db import models


class CarouselInfo(models.Model):
    image_link = models.CharField(max_length=100)
    image_header = models.CharField(max_length=100)
    image_description = models.CharField(max_length=500)

    def __str__(self):
        return self.image_header
