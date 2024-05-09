from django.db import models
from filter.models import Filter
from django.utils import timezone

class TuitionPost(models.Model):
    DURATION_CHOICES = [
        ('1_month', '1 Month'),
        ('2_months', '2 Months'),
        ('3_months', '3 Months'),
        ('6_months', '6 Months'),
        ('1_year', '1 Year'),
        ('not_fixed','not_fixed')
    ]

    DAYS_PER_WEEK_CHOICES = [
        (1, '1 Day/Week'),
        (2, '2 Days/Week'),
        (3, '3 Days/Week'),
        (4, '4 Days/Week'),
        (5, '5 Days/Week'),
        (6, '6 Days/Week'),
        (7, '7 Days/Week'),
    ]

    QUALIFICATION_CHOICES = [
        ('JSC', 'JSC'),
        ('SSC', 'SSC'),
        ('HSC', 'HSC'),
        ('Bachelor', 'Bachelor Degree'),
        ('Master', 'Master Degree'),
        ('PhD', 'PhD'),
        ('Other', 'Other Qualification'),
    ]

    duration = models.CharField(max_length=20, choices=DURATION_CHOICES)
    class_of_student = models.ForeignKey(Filter, on_delete=models.CASCADE)
    days_per_week = models.IntegerField(choices=DAYS_PER_WEEK_CHOICES)
    required_qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    description = models.TextField()
    creation_time = models.DateTimeField(default=timezone.now)  # Add creation time field

    
    def formatted_creation_time(self):
        return self.creation_time.strftime('%Y-%m-%d')

    def __str__(self):
        return f"{self.class_of_student.name} Tuition Post ({self.duration}, {self.days_per_week} days/week)"
