from django.db import models
from django.contrib.auth.models import User
from tuition.models import TuitionPost

class Application(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tuition_post = models.ForeignKey(TuitionPost, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} applied for {self.tuition_post.class_of_student}"