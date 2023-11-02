from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  intro = models.TextField()
  body = models.TextField()
  posted_date = models.DateField(auto_now_add=True)
  post_image = models.ImageField(upload_to='posts/images/', blank=True, null=True)

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  body = models.TextField()
  posteddate = models.DateTimeField(auto_now_add=True)