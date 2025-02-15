# Generated by Django 5.0.6 on 2024-07-23 12:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0008_rename_user_id_director_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.city')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Profile.director')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.district')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('arrival_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('taxi_to', models.BooleanField(default=False)),
                ('taxi_from', models.BooleanField(default=False)),
                ('toilet', models.BooleanField(default=False)),
                ('food', models.BooleanField(default=False)),
                ('drinks', models.BooleanField(default=False)),
                ('min_rating', models.IntegerField()),
                ('price', models.IntegerField()),
                ('publishing_date', models.DateField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.city')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.district')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.post')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Search.shops')),
            ],
        ),
    ]
