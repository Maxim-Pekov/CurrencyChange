from django.db import models

# Create your models here.
class Currency_converter(models.Model):
    currency_code = models.CharField(max_length=3)
    currency_quality = models.PositiveIntegerField()
    currency_name = models.CharField(max_length=20)
    currency_curs_by_rub = models.FloatField(max_length=10)


    def __str__(self):
        return f'{self.currency_code}'