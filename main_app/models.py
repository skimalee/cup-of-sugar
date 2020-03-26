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
    user1_id = models.IntegerField()
    user1_name = models.CharField(max_length=50)
    user2_id = models.IntegerField()
    user2_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chat between {self.user1_name}, {self.user2_name}"


class Message(models.Model):
    content = models.CharField(max_length=160)
    sender_name = models.CharField(max_length=50)
    sender_id = models.IntegerField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    zip = models.IntegerField()
    chats = models.ManyToManyField(Chat)
    cups_filled = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return str(self.user)

class Cup(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, default='')
    zip = models.IntegerField(default=0)
    fulfilled_by_profile_id = models.IntegerField(default=0)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        print(reverse('detail', kwargs={'pk': self.id}))
        return reverse('detail', kwargs={'pk': self.id})

    def __str__(self):
        return f"{self.cup_type} cup {self.item} in {self.get_category_display()} is {'fulfilled' if self.fulfilled else 'not fulfilled'}"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    cup = models.ForeignKey(Cup, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cup_id: {self.cup_id} @{self.url}"