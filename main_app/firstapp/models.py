from django.db import models
from django.utils.text import slugify
# Create your models here.
class Register(models.Model):

    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    psw=models.CharField(max_length=20)
    pswr=models.CharField(max_length=20)

    def __str__(self):
        return self.name




class Meal(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    categery=models.ForeignKey('Categery',on_delete=models.SET_NULL, null=True)
    people=models.IntegerField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    #preptime=models.IntegerField()
    image=models.ImageField(upload_to='firstapp/')
    #slug=models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name='meal'
        verbose_name_plural='meals'

    def __str__(self):
        return self.name



class Categery(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name='categery'
        verbose_name_plural='categeries'

    def __str__(self):
        return self.name
        return self.name