# Generated by Django 4.0.8 on 2022-10-31 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]