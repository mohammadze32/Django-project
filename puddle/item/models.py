from django.contrib.auth.models import User
from django.db import models
class Catagory(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ('name' ,)
        verbose_name_plural = 'Categories'
    def  __str__(self):
        return self.name
class Item(models.Model):
    catagory = models.ForeignKey(Catagory , related_name='items' , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True , null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_image' , blank=True , null=True)
    is_sold = models.BooleanField(default=False)
    create_bt = models.ForeignKey(User , related_name='items' , on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
