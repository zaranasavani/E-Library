# Generated by Django 4.2.1 on 2024-08-03 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='piece',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='piece',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='piece',
            name='publisher',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
