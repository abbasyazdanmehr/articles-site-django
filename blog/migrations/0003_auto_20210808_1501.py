# Generated by Django 3.0.14 on 2021-08-08 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210808_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='condition',
            new_name='status',
        ),
    ]
