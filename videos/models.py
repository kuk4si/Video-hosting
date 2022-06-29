from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.utils import timezone

User = get_user_model()


class Video(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to='videos', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)
    preview_pic = models.ImageField(upload_to='previews')
