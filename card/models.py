from django.db import models

class Card(models.Model):
  id = models.CharField(max_length=255, primary_key=True)
  card_title = models.CharField(max_length=255)
  house = models.CharField(max_length=255)
  card_type = models.CharField(max_length=255)
  front_image = models.CharField(max_length=255)
  card_text = models.CharField(max_length=255)
  traits = models.CharField(max_length=255, null=True)
  amber = models.IntegerField()
  power = models.IntegerField()
  armor = models.IntegerField()
  rarity = models.CharField(max_length=255)
  flavor_text = models.CharField(max_length=255, null=True)
  card_number = models.IntegerField()
  expansion = models.IntegerField()
  is_maverick = models.BooleanField()