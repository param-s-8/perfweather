from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='cities'
    
class DeetCity(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='cities'

class Feedback(models.Model):
    customer_name=models.CharField(max_length=120)
    customer_email=models.EmailField()
    customer_country=models.CharField(max_length=30)
    review=models.TextField()
    happy=models.BooleanField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
