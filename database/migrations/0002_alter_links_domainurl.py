# Generated by Django 5.0.1 on 2024-03-19 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='domainURL',
            field=models.CharField(max_length=255),
        ),
    ]
