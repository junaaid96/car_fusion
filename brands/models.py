from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    founded_year = models.PositiveIntegerField()
    headquarters = models.CharField(max_length=255)
    website = models.URLField()

    def __str__(self):
        return self.name
