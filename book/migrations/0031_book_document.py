# Generated by Django 4.0.8 on 2022-12-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0030_book_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='document',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]
