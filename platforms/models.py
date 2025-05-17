from django.db import models


class Platform(models.Model):
    """
    Model representing a platform.
    """
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
