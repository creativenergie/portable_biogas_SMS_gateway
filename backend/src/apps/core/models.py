from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    mobile_num = models.CharField(max_length=50, unique=True, null=True)
    date_of_birth = models.DateField(null=True)
    # Mapped in domain.UserGender
    gender = models.PositiveSmallIntegerField(null=True)

    class Meta:
        db_table = "user"
        indexes = [models.Index(fields=["mobile_num"])]


class Administrator(User):
    class Meta:
        proxy = True


class Consumer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    supplier = models.ForeignKey("Supplier", on_delete=models.DO_NOTHING, null=True)
    mobile_num = models.CharField(max_length=50, unique=True, null=True)
    geolocation = JSONField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "consumer"


class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    mobile_num = models.CharField(max_length=50, unique=True, null=True)
    geolocation = JSONField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "supplier"
