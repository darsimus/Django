from django.db import models

class Pokemon(models.Model):
    id=models.CharField(max_length=10, primary_key=True)
    name=models.CharField(max_length=20, null=False)
    hp=models.IntegerField(null=True)
    types=models.JSONField(max_length=255, null=True)
    abilities=models.CharField(max_length=255, null=True)
    weaknesses=models.JSONField(max_length=255, null=True)
    resistances=models.CharField(max_length=255, null=True)
    convertedRetreatCost=models.CharField(max_length=255,null=True)
    artist=models.CharField(max_length=255, null=True)
    rarity=models.CharField(max_length=255, null=True)
    flavorText=models.CharField(max_length=400, null=True)
    small_images=models.JSONField(max_length=255, null=True)
    big_images=models.JSONField(max_length=255, null=True)

    def __str__(self):
        return f'{self.name}'

    

# Create your models here.
