from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    result = models.TextField(max_length=20)

    def __str__(self):
        return self.user.username 
