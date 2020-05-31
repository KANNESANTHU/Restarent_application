from django.db import models

# Create your models here.
class Reservation(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    n_persons=models.IntegerField()
    n_date=models.DateField()
    n_time=models.TimeField()

    class Meta:
        verbose_name='reservation'
        verbose_name_plural='reservations'

    def __str__(self):
        return self.name