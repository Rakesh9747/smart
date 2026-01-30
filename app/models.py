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
