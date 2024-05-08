from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tutor/images/')
    mobile_no = models.CharField(max_length=12)
    description = models.TextField(blank=True)
    experience = models.CharField(max_length=100, blank=True)
    educational_qualification = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
