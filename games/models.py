from django.db import models


# class Game(models.Model):
#     """
#     Model representing a game.
#     """
#     title = models.CharField(max_length=255)
#     description = models.TextField(null=True, blank=True)
#     release_year = models.IntegerField(null=True, blank=True)
#     genre = models.ForeignKey('genres', on_delete=models.SET_NULL, related_name='games')
#     developer = models.ForeignKey('developers', on_delete=models.SET_NULL, related_name='games')
#     platform = models.ForeignKey('platforms', on_delete=models.SET_NULL, related_name='games')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     def __str__(self):
#         return self.username