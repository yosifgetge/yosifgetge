from django.db import models
class Login(models.Model):
    username = models.CharField(max_length=25,null=False)
    password = models.CharField(max_length=100,null=False)
    Active = models.BooleanField(default=True)
