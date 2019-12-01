from django.db import models

# Create your models here.

class Article(models.Model):
    titre      = models.CharField(max_length=255)
    contenu    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    auteur     = models.IntegerField()

    def __str__(self):
        return self.titre
