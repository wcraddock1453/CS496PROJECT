from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

# model criteria for photo descriptions
class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(default="Aman")
    Height=models.FloatField(default=0.00)
    HairColor=models.TextField(default="Aman")
    HairType=models.TextField(default="Aman")
    EyeColor=models.TextField(default="Aman")
    Glasses=models.TextField(default="Aman")
    Scar=models.TextField(default="Aman")

    def __str__(self):
        return self.description