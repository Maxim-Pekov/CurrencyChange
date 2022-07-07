from django.db import models

# Create your models here.
class currency_converter(models.Model):
    currency_code = models.CharField(max_length=3)
    currency_quality = models.PositiveIntegerField(max_length=1000)
    currency_name = models.CharField(max_length=20)
    currency_curs_by_rub = models.FloatField(max_length=10)


    def __str__(self):
        return f'{self.currency_code} - {self.currency_name}'