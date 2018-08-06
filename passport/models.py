from django.db import models

class Your_Park(models.Model):
    username = models.CharField(max_length=128)
    park_name = models.CharField(max_length=128)
    park_description = models.TextField()

    def __str__(self):
        return f"{self.park_name}"

class Park_Review(models.Model):
    username = models.CharField(max_length=128)
    park_name = models.CharField(max_length=128)
    review = models.TextField()

class Friend(models.Model):
    username = models.CharField(max_length=128)
    friend = models.CharField(max_length=128)
