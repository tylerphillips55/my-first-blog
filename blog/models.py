from django.db import models
from django.utils import timezone

class Post(models.Model):                                               #each model is a subclass of Model; maps to a single db table
                                                                        #each field is an instance of a Field class
    author = models.ForeignKey('auth.User')                             #relationship field; argument is class to which model relates to
    title = models.CharField(max_length = 200)                          #string field for small-large sized strings
    text = models.TextField()                                           #large text field
    created_date = models.DateTimeField(default = timezone.now)         #date and time represented by instance of another class
    published_date = models.DateTimeField(blank = True, null = True)    #blank and null are field options, optional arguments available to all field types
                                                                        #   if null = True, Django stores empty values as NULL in db; if blank = True, field can be blank
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
