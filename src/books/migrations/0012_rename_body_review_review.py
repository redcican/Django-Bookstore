# Generated by Django 3.2.4 on 2021-06-05 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20210605_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='body',
            new_name='review',
        ),
    ]