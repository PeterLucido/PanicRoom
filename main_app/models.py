from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Fear(models.Model):
  name = models.CharField(max_length=15)
  description = models.TextField(max_length=250)
  conquered = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('fear-detail', kwargs={'fear_id': self.id})

class Photo(models.Model):
  url = models.CharField(max_length=200)
  fear = fear = models.OneToOneField(Fear, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for fear_id: {self.fear_id} @{self.url}"