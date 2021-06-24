from django.db import models

# Create your models here.
class userlogin(models.Model):
    lname = models.CharField(max_length=42)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    ladd = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.lname}  |  {self.email}  |  {self.ladd}"