from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True)
    birth_day = models.DateField(blank=True, null=True)
    father_name = models.CharField(blank=True, null=True, max_length=150)
    telegram_id = models.IntegerField(blank=True, null=True, unique=True)
    phone = models.CharField(unique=True, max_length=20)
    post = models.ForeignKey(to='Post', on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(to='City', on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(to='District', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=100)
    status = models.BooleanField(default=True)
    is_director = models.BooleanField(default=False)
    subs = models.BooleanField(default=False)
    end_subs = models.DateField(blank=False, null=True)


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)


class District(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(to='City', on_delete=models.CASCADE)


class Post(models.Model):
    name = models.CharField(max_length=30)


class Director(models.Model):
    user = models.ForeignKey(to='Profile.User', on_delete=models.CASCADE)
