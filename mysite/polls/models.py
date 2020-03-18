import datetime

from django.db import models
from django.utils import timezone
# this creates the classes in the database
# let them know that this app is poppin --> settings.py polls.apps.PollsConfig
# makemigrations polls
# then alter to database --> sqlmigrate polls 0001
# finally migrate

# now you can check things by using the API --> shell


class Question(models.Model):
  question_text = models.CharField(max_length=200)  # must give a maxlength for Charfields
  pub_date = models.DateTimeField('date published') # this gives humans a name, instead of pub_date

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)  # for each choice, it will match with one question
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text