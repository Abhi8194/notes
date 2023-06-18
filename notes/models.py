from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE_TYPES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]
    
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=10, choices=NOTE_TYPES, default=TEXT)
    file = models.FileField(upload_to='notes/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

