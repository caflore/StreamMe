from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Vod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    vod = models.FileField(upload_to='vods')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app-vod-detail', kwargs={'pk': self.pk})