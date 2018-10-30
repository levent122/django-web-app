from django.db import models
from realtors.models import Realtor

class Product(models.Model):

    realtor = models.ForeignKey(Realtor,on_delete= models.DO_NOTHING,related_name='realtor')
    title = models.CharField(max_length= 200)
    address = models.CharField(max_length= 200)
    city = models.CharField(max_length= 100)
    district = models.CharField(max_length= 100)
    description = models.TextField()
    status = models.CharField(max_length= 50)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    product_age = models.FloatField()
    photo_main = models.ImageField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField()
    photo_3 = models.ImageField()
    photo_4 = models.ImageField()
    photo_5 = models.ImageField(blank=True)
    photo_6 = models.ImageField(blank=True)
    photo_7 = models.ImageField(blank=True)
    photo_8 = models.ImageField(blank=True)
    photo_9 = models.ImageField(blank=True)
    photo_10 = models.ImageField(blank=True)
    is_published = models.BooleanField(default= True)
    date = models.DateTimeField()
    def __str__(self):
        return self.title