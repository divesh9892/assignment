from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FileUpload(models.Model):
    desc = models.TextField()
    file = models.FileField(upload_to='media')
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

