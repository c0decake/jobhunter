from django.db import models


class Orders(models.Model):
    shop = models.ForeignKey(to='Shops', on_delete=models.CASCADE)
    district = models.ForeignKey(to='Profile.District', on_delete=models.CASCADE)
    city = models.ForeignKey(to='Profile.City', on_delete=models.CASCADE)
    date = models.DateField()
    arrival_time = models.TimeField()
    end_time = models.TimeField()
    taxi_to = models.BooleanField(default=False)
    taxi_from = models.BooleanField(default=False)
    toilet = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    drinks = models.BooleanField(default=False)
    min_rating = models.IntegerField()
    post = models.ForeignKey(to='Profile.Post', on_delete=models.CASCADE)
    price = models.IntegerField()
    publishing_date = models.DateField()
    director = models.ForeignKey(to='Profile.User', on_delete=models.CASCADE)


class Shops(models.Model):
    name = models.CharField(max_length=150)
    city = models.ForeignKey(to='Profile.City', on_delete=models.CASCADE)
    district = models.ForeignKey(to='Profile.District', on_delete=models.CASCADE)
    director = models.ForeignKey(to='Profile.Director', on_delete=models.SET_NULL, null=True)
