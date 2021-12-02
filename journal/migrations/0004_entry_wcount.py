# Generated by Django 3.2 on 2021-12-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_rename_name_entry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='wcount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
