from django.db import models 

class Profile(models.Model):
    image = models.ImageField(upload_to='uploads/index/')
