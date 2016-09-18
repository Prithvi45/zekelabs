from django.db import models

# Create your models here.

from django.db import models

class RegisterProfile(models.Model):
    # user = models.OneToOneField("auth.User")
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=15,null=True)
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __unicode__(self):
        return self.subject + ' ' + self.mobile