from django.db import models

class District(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название района')
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'districts'

class Theatre(models.Model):
    url = models.CharField(max_length=20, verbose_name='URL театра')
    name = models.CharField(max_length=20, verbose_name='Название театра')
    id = models.IntegerField(primary_key=True)
    information = models.TextField(verbose_name='Информация')
    image_source = models.CharField(max_length=30)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'theatres'

class Perfomance(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название постановки')
    id = models.IntegerField(primary_key=True)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'perfomances'
