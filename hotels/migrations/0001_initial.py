# Generated by Django 3.2.3 on 2021-05-21 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(db_index=True, max_length=124)),
                ('hotel_description', models.CharField(db_index=True, max_length=124)),
                ('hotel_country', models.CharField(max_length=124)),
                ('hotel_phone', models.CharField(max_length=12)),
                ('hotel_season_open_day', models.DateField(auto_now_add=True, db_index=True)),
                ('hotel_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
