# Generated by Django 4.1.7 on 2023-03-12 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='InternshipDuration',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]