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

class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    messager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Chat between {self.owner}, {self.messager}"

class Message(models.Model):
    content = models.CharField(max_length=160)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

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

    def __str__(self):
        return f"{self.cup_type} cup {self.item} in {self.category} is {'fulfilled' if self.fulfilled else 'not fulfilled'}"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50) 
    zipcode = models.IntegerField(max_length=5) 
    email = models.EmailField()

    def __str__(self):
        return self.user

