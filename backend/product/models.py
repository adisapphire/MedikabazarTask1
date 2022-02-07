from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=1000,blank=False,null=False)
    quantity = models.IntegerField(default=0,
                                    validators=[MaxValueValidator(100000000),MinValueValidator(0)])
    price = models.DecimalField(max_digits=6, decimal_places=2,default=0,null=False)
    is_active = models.BooleanField(default=True, blank=False,null=False)
    brand = models.CharField(max_length=1000,blank=True,null=True)


    def __str__(self):
        return self.name


