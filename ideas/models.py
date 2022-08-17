from django.db import models

# Create your models here.

class Ideas(models.Model):
    text = models.CharField('Идея', max_length=150)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'idea'
        verbose_name_plural = 'ideas'
