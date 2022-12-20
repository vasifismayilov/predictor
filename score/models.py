from django.db import models

# Create your models here.
class Login_user(models.Model):
    number = models.CharField(max_length=8)
    password = models.CharField(max_length=2500)
    # show = models.BooleanField(default=False)
    
    def __str__(self):
        return self.number