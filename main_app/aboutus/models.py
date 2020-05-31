from django.db import models

# Create your models here.
class Aboutus(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    #image=models.ImageField(upload_to='aboutus/')

    class Meta:
        verbose_name='aboutus'
        verbose_name_plural='aboutus'

    def __str__(self):
        return self.title

class Why_choose_us(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()

    class Meta:
        verbose_name = 'why_choose_us'
        verbose_name_plural ='why_choose_us'

    def __str__(self):
        return self.title


class Chef(models.Model):
    name=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    content=models.TextField()
    image=models.ImageField(upload_to='chef/')

    class Meta:
        verbose_name = 'chef'
        verbose_name_plural ='chef'

    def __str__(self):
        return self.name
