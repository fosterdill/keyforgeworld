# Generated by Django 2.1.5 on 2019-01-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='traits',
            field=models.CharField(max_length=255, null=True),
        ),
    ]