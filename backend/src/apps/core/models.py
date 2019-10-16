from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    mobile_num = models.CharField(max_length=50, unique=True, null=True)
    date_of_birth = models.DateField(null=True)
    # Mapped in domain.UserGender
    gender = models.PositiveSmallIntegerField(null=True)

    class Meta:
        db_table = "user"
        indexes = [models.Index(fields=["mobile_num"])]
