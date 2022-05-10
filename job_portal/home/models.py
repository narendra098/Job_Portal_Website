from statistics import mode
from django.db import models

# Create your models here.
class Website_Users(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    mail = models.EmailField()
    password = models.CharField(max_length=10)
    type_of_user = models.CharField(max_length=20)

    def __str__(self):
        return self.name