from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Like(models.Model):

    user = models.ForeignKey('auth.User', on_delete= models.DO_NOTHING, related_name='likes')
    product = models.ForeignKey(Product, on_delete= models.DO_NOTHING, related_name='liked_products')
    date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return '%s'%(self.product)