# Generated by Django 3.2.7 on 2022-08-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ideas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Идея')),
            ],
            options={
                'verbose_name': 'idea',
                'verbose_name_plural': 'ideas',
            },
        ),
    ]
