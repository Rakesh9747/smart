from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    accreditation = models.IntegerField(default=0)
    website_valid = models.IntegerField(default=0)
    reviews_count = models.IntegerField(default=0)
    placement_score = models.IntegerField(default=0)
    website = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    def __str__(self):
        return self.name

from django.db import models

class Institution(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField()
    accreditation = models.IntegerField()
    website_valid = models.IntegerField()
    reviews_count = models.IntegerField()
    placement_score = models.IntegerField()
    website = models.URLField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class StudentApplication(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name


class AdminUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
