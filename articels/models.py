from django.db import models
class Articles(models.Model):
    titile=models.CharField(max_length = 100 )
    slug=models.SlugField()
    post=models.TextField()
    thumbnile = models.ImageField(default='defualt.png', blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titile
# Create your models here.
