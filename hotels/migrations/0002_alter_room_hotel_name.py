# Generated by Django 3.2.3 on 2021-05-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hotel_name',
            field=models.CharField(db_index=True, help_text='Комментарий для ввода', max_length=124, verbose_name='Название номера: '),
        ),
    ]
