from django.db import models
from django.utils import timezone

class Broast(models.Model):
    is_roast = models.BooleanField()
    content = models.CharField(max_length=280)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
# One model to represent both boasts and roasts
# Boolean to tell whether it's a boast or a roast
# CharField to put the content of the post in
# IntegerField for up votes
# IntegerField for down votes
# DateTimeField for submission time