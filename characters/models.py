from django.db import models


role_choices = [
    ('hero', 'Hero'),
    ('villain', 'Villain'),
    ('support', 'Support'),
    ('anti-hero', 'Anti-Hero'),
    ('neutral', 'Neutral'),
    ('rival', 'Rival'),
    ('antagonist', 'Antagonist'),
    ('npc', 'NPC'),
]


class Character(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    game = models.ForeignKey('games.Game', on_delete=models.PROTECT, related_name='characters')
    role = models.CharField(max_length=50, choices=role_choices, default='hero')
    is_playable = models.BooleanField(default=True)
    image_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
