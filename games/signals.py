from django.db.models.signals import post_save
from django.dispatch import receiver

from games.models import Game
from utils.langchain_api.chains import get_game_description


@receiver(post_save, sender=Game)
def game_post_save(sender, instance, **kwargs):
    """
    Signal to handle actions after a Game instance is saved.
    """
    description_ia = get_game_description(instance.title)
    instance.description = description_ia
    instance.save()
