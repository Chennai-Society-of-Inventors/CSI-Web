from django.db import models


class CarouselInfo(models.Model):
    image_link = models.CharField(max_length=100)
    image_header = models.CharField(max_length=100)
    image_description = models.CharField(max_length=500)

    def __str__(self):
        return self.image_header


class ProblemInfo(models.Model):
    problem_category = models.CharField(max_length=100)
    problem_description = models.CharField(max_length=500)
    name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=15)
    contact_address = models.CharField(max_length=100)
    email_id = models.EmailField()

    def __str__(self):
        return self.problem_category + " by " + self.name


class InventionInfo(models.Model):
    invention = models.CharField(max_length=100)
    abstract = models.CharField(max_length=500)
    team_details = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=15)
    email_id = models.EmailField()

    def __str__(self):
        return self.invention
