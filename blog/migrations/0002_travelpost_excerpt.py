# Generated by Django 4.2.15 on 2024-08-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelpost',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
