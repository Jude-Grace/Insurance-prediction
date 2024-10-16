from django.db import models

# Create your models here.
class ckdModel(models.Model):

    AGE=models.FloatField()
    BMI=models.FloatField()
    CHILDREN=models.FloatField()
    GENDER_M1_F0=models.FloatField()
    SMOKER_Y1_N0=models.FloatField()
