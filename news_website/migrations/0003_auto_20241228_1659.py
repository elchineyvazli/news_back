# Generated by Django 2.2.8 on 2024-12-28 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_website', '0002_auto_20241228_1653'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='news',
            table='EditorsPicks',
        ),
    ]
