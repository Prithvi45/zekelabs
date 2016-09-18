from django.db import models

# Create your models here.

from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=15,null=True)
    subject = models.TextField()
    