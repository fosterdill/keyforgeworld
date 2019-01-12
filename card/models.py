from django.db import models

class Card(models.Model):
  id = models.CharField(max_length=255, primary_key=True)
  number = models.IntegerField()
  name = models.CharField(max_length=255)
  house = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  rarity = models.CharField(max_length=255)
  aember = models.IntegerField(null=True)
  power = models.IntegerField(null=True)
  armor = models.IntegerField(null=True)
  traits = models.CharField(max_length=255, null=True)
  keywords = models.CharField(max_length=255, null=True)
  text = models.CharField(max_length=255, null=True)
  imageurl = models.CharField(max_length=255)
  artist = models.CharField(max_length=255, null=True)
  setsku = models.CharField(max_length=255)
