# Generated by Django 3.1.2 on 2020-10-11 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20201011_0001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thingtodo',
            options={'ordering': ['-created_at']},
        ),
    ]
