from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

CATEGORIES = (
    ('A', 'Food'),
    ('B', 'Homegoods'),
    ('C', 'Pets'),
    ('D', 'Kids'),
    ('E', 'Lawn'),
    ('F', 'Services'),
    ('G', 'Other')
)

CUP_TYPE = (
    ('1', 'Empty'),
    ('2', 'Extra')
)

# Create your models here.


class Cup(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cup_type = models.CharField(
        max_length=1,
        choices=CUP_TYPE
    )
    item = models.CharField(max_length=100)
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES
    )
    fulfilled = models.BooleanField(default=False)
