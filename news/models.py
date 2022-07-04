from django.db import models
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=150)
    image = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='Изображение')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('articles_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
