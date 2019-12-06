from django.db import models

# Create your models here.

class User(models.Model):
    login      = models.CharField(max_length=255, unique=True)
    password   = models.CharField(max_length=255)
    nom        = models.CharField(max_length=255)
    prenom     = models.CharField(max_length=255)
    email      = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "{} {}".format(self.prenom, self.nom)

