from django.contrib.auth import get_user_model
from django.db import models
from django import forms

# Create your models here.


class Moto(models.Model):
    moto_brands = ['KTM', 'YAMAHA', 'Ducati', 'Suzuki',
                   'BETA', 'Husqvarna', 'Honda', 'BMW',
                   'Aprilia', 'Kawasaki', 'Energica',
                   'MV Agusta', 'Triumph']
    years = [2022 - i for i in range(23)]

    model = models.CharField(max_length=64)
    brand = models.CharField(label='Brand', widget=forms.Select(choices=moto_brands))
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    engine_size = models.CharField(max_length=4)
    year = models.CharField(label='Year', max_length=4, widget=forms.Select(choices=years))

    def __str__(self):
        return self.model
