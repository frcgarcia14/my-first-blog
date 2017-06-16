from django.db import models
from django.utils import timezone

# Here I defined a new class for create the Posts of the blog
class Post(models.Model):
     # and here there are the attributes of the class
     # that are common for each post
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # and now here I defined the methods for this class
    def publish(self): # this is for publish the post
        self.published_date = timezone.now() # first I stablish the date for the new created post
        self.save() # and then I save it inside the database.
    def __str__(self): # get the post title as string
        return self.title
