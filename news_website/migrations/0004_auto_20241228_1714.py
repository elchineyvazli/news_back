# Generated by Django 2.2.8 on 2024-12-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_website', '0003_auto_20241228_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tag',
            field=models.CharField(max_length=20),
        ),
    ]