# Generated by Django 5.1.3 on 2024-12-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(max_length=2083),
        ),
    ]
