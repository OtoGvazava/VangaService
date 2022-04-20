from django.db import models


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    mainImage = models.TextField(null=True)
    variantsString = models.TextField(null=True)
    drawFunction = models.TextField(null=True)
    publish_datetime = models.DateTimeField()
