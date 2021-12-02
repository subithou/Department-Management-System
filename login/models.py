from django.db import models


class login_table(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    category = models.CharField(max_length=20)

