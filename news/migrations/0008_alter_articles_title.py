# Generated by Django 3.2.7 on 2022-07-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_articles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]
