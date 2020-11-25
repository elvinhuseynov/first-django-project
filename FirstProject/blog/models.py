from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.Charfield(max_length=20)
    description = models.Textfield


