# Generated by Django 3.2 on 2021-11-29 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='name',
            new_name='title',
        ),
    ]
