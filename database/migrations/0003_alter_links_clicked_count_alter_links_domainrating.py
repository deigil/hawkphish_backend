# Generated by Django 5.0.3 on 2024-04-02 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_links_domainurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='clicked_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='links',
            name='domainRating',
            field=models.IntegerField(),
        ),
    ]