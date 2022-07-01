from django.db import models
from django.contrib.auth import get_user_model 
user=get_user_model()

# Create your models here.

class Link(models.Model):
    target_url = models.URLField(max_length = 200)
    description = models.CharField(max_length = 200)
    identifier = models.SlugField(
        max_length= 20, blank =True, unique = True
    )
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    active = models.BooleanField(default = True)


