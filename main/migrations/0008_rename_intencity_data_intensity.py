# Generated by Django 4.2.7 on 2023-11-19 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_data_relevance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='intencity',
            new_name='intensity',
        ),
    ]
