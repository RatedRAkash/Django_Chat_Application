from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


    # eita mane Backend ee naile Object Save korle <Object(...)> eivabe SAVE korbe... jeita amra chai Nah...
    # so, amra Object jeno dekhte "name" er moto DB te dekhay tai __str__(self) function use kora huise
    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    # eita mane Backend ee naile Object Save korle <Object(...)> eivabe SAVE korbe... jeita amra chai Nah...
    # so, amra Object jeno dekhte "name" er moto DB te dekhay tai __str__(self) function use kora huise
    def __str__(self):
        return f'{self.id}'+". "+self.content[:11]+"..."+ "(" + f'{self.user.username}' + ") --->" + f'{self.room.name}'