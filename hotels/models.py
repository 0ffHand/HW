from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    hotel_name = models.CharField(max_length=124,
                                  db_index=True,
                                  verbose_name="Название номера: ",
                                  help_text="Комментарий для ввода")
    hotel_description = models.CharField(max_length=124, db_index=True)
    hotel_country = models.CharField(max_length=124)
    hotel_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_phone = models.CharField(max_length=12)
    hotel_season_open_day = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.hotel_name
