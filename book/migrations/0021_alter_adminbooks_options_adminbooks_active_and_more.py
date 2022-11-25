# Generated by Django 4.0.8 on 2022-11-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0020_remove_book_time_remove_review_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminbooks',
            options={'permissions': [('AdminBksPermissions', 'Can add AdminBooks')]},
        ),
        migrations.AddField(
            model_name='adminbooks',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='adminbooks',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
