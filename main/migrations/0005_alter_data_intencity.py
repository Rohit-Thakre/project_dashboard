# Generated by Django 4.2.7 on 2023-11-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_data_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='intencity',
            field=models.CharField(max_length=10, null=True),
        ),
    ]