# Generated by Django 4.1.6 on 2023-02-04 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='complex',
            new_name='complete',
        ),
    ]
