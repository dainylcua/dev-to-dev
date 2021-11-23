from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField 

class Topic(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    date = models.DateField('date_published', auto_now=True)

    def get_absolute_url(self):
        return reverse('index')
    
    def __str__(self):
      return f"{self.title} is topic number {self.id}"

class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    score = models.IntegerField(default=0, editable=False)
    admin = models.BooleanField(default=False, editable=False)
    date = models.DateField('date_published', auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    
    def __str__(self):
      return f"{self.title} is under topic {self.topic}"

class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    score = models.IntegerField(default=0, editable=False)
    date = models.DateField('date_published', auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_comment_display()} on {self.date}'
        

    # class Meta:
    #     ordering = ('-date',)
        

# class User(models.Model):
#     id = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.CharField(max_length=50)
#     username = models.TextField(max_length=250)
#     password = models.CharField(max_length=50)
#     is_admin = admin = models.BooleanField()

#     def __str__(self):
#         return self.id

#     def get_absolute_url(self):
#         return reverse('detail', kwargs={'pk': self.id})



# Create your models here.
