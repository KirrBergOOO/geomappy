# Generated by Django 3.2.7 on 2022-07-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_articles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
