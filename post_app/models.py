from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=125)
    context = models.TextField()


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name="post_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return str(self.image)
