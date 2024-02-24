from django.db import models

class Proverb(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        l = len(self.text)
        return self.text[:(30 if l > 30 else l)] + '...'
