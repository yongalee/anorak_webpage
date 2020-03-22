from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    thumbnail = models.ImageField(upload_to='static/uploads/')
    body = models.TextField()

    def __str__(self):
        return self.title