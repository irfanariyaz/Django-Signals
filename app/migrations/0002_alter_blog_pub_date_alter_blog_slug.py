# Generated by Django 5.1.2 on 2024-10-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]