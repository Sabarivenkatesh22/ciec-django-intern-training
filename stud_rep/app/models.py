from django.db import models

# Create your models here.
from django.db import models

class student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id   = models.EmailField(null=False)

