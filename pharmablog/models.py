from django.db import models

# Create your models here.
class Article(models.Model):
    Sujet = models.CharField(max_length = 255)
    Contenu = models.TextField()
    Autheur = models.ForeignKey('Author')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.Sujet


class Author(models.Model):
    nom = models.CharField(max_length = 100)
    bio = models.TextField()

    def __str__(self):
        return self.Nom
