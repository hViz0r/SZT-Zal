from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'
    title = models.CharField('title', max_length=255)
    text = models.TextField('text')
    author = models.ForeignKey(User, related_name='news', verbose_name='author')
    created = models.DateTimeField('created', auto_now_add=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField('title', max_length=255)
    numberOfPlayers = models.TextField('number of players')
    owner = models.ForeignKey(User, related_name='game', verbose_name='owner')
    created = models.DateTimeField('created', auto_now_add=True)

    def __str__(self):
        return self.title


class Member(models.Model):
    user = models.OneToOneField(User)
    rank = models.TextField('rank', default='Członek')
    whFaction = models.TextField('faction', default='Brak')

    def __str__(self):
        return self.user.username

