from django.db import models

class Theatre(models.Model):
    url = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    information = models.TextField()
    image_source = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'theatres'