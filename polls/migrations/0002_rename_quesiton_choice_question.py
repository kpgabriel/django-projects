# Generated by Django 3.2.4 on 2021-07-12 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='quesiton',
            new_name='question',
        ),
    ]
