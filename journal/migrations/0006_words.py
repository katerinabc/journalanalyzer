# Generated by Django 3.2 on 2021-12-01 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_alter_entry_wcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='words',
            fields=[
                ('title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='journal.entry')),
                ('word', models.TextField()),
            ],
        ),
    ]
