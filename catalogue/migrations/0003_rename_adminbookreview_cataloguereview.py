# Generated by Django 4.0.8 on 2022-11-24 22:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0002_retured'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminBookReview',
            new_name='CatalogueReview',
        ),
    ]
