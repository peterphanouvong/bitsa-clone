import datetime

from django.db import models
from django.utils import timezone

EVENT_STATUS = (
    ('CURRENT','Current'),
    ('PAST', 'Past'),
)

PORTFOLIO = (
  ('SOCIAL', 'Social'),
  ('EDUCATION', 'Education'),
  ('CAREERS','Careers'),
  ('GENERAL','General')
)

# Create your models here.
class Blog(models.Model):
  blog_title = models.CharField(max_length=200, default = 'blah')
  description_text = models.CharField(max_length=500)
  pub_date = models.DateField('date published')
  image = models.ImageField(upload_to='images/')
  blog_content = models.TextField(max_length=100000)
  
  def __str__(self):
    return '%s - %s' % (self.blog_title, self.pub_date)

class Profile(models.Model):
  position = models.CharField(max_length=200)
  name = models.CharField(max_length=500)
  image = models.ImageField(upload_to='images/profile')
  year = models.CharField(max_length=4)
  email = models.EmailField(max_length=500, null=True)
  degree = models.CharField(max_length=500, null=True)
  hobby = models.CharField(max_length=500, null=True)
  one_word = models.CharField(max_length=500, null=True)
  linkedin = models.CharField(max_length=1000, null=True)
  
  def __str__(self):
    return '%s - %s - %s' % (self.name, self.year, self.position)

class Sponsor(models.Model):
  sponsor = models.CharField(max_length=500)
  image = models.ImageField(upload_to='images/sponsor')
  description = models.TextField(max_length=1000)
  link = models.URLField(max_length=1000)
  type_of_sponsor = models.CharField(max_length=500, null=True)
  
  def __str__(self):
    return self.sponsor

class Events(models.Model):
  title = models.CharField(max_length=200)
  date = models.DateField('date of event')
  time = models.CharField(max_length=8)
  location = models.CharField(max_length=200)
  cover_photo = models.ImageField(upload_to='images/events')
  description = models.TextField(max_length=1000)
  link = models.URLField(max_length=1000)
  current_or_past = models.CharField(max_length=250, null=False, choices=EVENT_STATUS, default='CURRENT')
  portfolio = models.CharField(max_length=250, null=False, choices=PORTFOLIO, default='GENERAL')


  def __str__(self):
    return '%s - %s - %s' % (self.title, self.current_or_past, self.date)


#1. Makemigrations blog i.e. python manage.py makemigrations blog
#2. SQL migrate blog with sequence number i.e. python manage.py sqlmigrate blog 0001
#3. Migrate i.e. python manage.py migrate