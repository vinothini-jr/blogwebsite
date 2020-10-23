from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    tags=TaggableManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    post_date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()

    def __str__(self):
        return '%s-%s' %(self.post.title,self.name)

'''class Tag(models.Model):
    post=models.ForeignKey(Post,related_name='tags',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    title =models.TextField()

    def __str__(self):
        return self.title'''

class Profile(models.Model):
    #postt = models.ForeignKey(Post, related_name='tags', on_delete=models.CASCADE)
    user=models.OneToOneField(User,null=True,related_name='profile',on_delete=models.CASCADE)
    img_pic=models.ImageField(null=True,blank=True,upload_to="images/")
    name=models.CharField(max_length=100,blank=True)
    bio=models.TextField(null=True)
    fb_url=models.CharField(max_length=100,blank=True)
    insta_url=models.CharField(max_length=100,blank=True)
    #twitter_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.user)

class register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()



