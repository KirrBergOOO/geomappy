# Generated by Django 3.2.7 on 2022-06-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
