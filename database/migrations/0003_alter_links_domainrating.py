# Generated by Django 5.0.2 on 2024-03-19 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_links_domainurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='domainRating',
            field=models.IntegerField(),
        ),
    ]
