# Generated by Django 3.2.7 on 2022-08-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideas',
            name='text',
            field=models.CharField(max_length=150, verbose_name='Идея'),
        ),
    ]
