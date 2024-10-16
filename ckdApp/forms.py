from django import forms
from .models import *


class ckdForm(forms.ModelForm):
    class Meta():
        model=ckdModel
        fields=['AGE','BMI','CHILDREN','GENDER_M1_F0','SMOKER_Y1_N0']
