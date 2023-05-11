from django.db import models

class Journalist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{ self.first_name } { self.last_name }"

class Article(models.Model):
    #author = models.CharField(max_length=50)
    author = models.ForeignKey(Journalist,on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=70)
    body = models.TextField()
    location = models.CharField(max_length=40)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.author } { self.title }"
    
