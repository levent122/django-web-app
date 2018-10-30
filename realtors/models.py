from django.db import models
from django.contrib.auth.models import User


class Realtor(models.Model):
  user = models.ForeignKey(User,on_delete= models.DO_NOTHING,related_name='realtors')
  name = models.CharField(max_length= 100)
  photo = models.ImageField()
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=100)
  facebook = models.CharField(max_length=100)
  twitter = models.CharField(max_length=100)
  instagram = models.CharField(max_length=100)
  is_mvp = models.BooleanField(default=False)
  date = models.DateTimeField()
  def __str__(self):
    return self.name
