# Generated by Django 3.0.8 on 2020-07-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searches'},
        ),
        migrations.AlterField(
            model_name='search',
            name='created',
            field=models.DateTimeField(verbose_name='Date Searched'),
        ),
    ]
