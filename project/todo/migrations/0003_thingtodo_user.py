# Generated by Django 3.1.1 on 2020-09-21 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_remove_thingtodo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='thingtodo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='auth.user'),
            preserve_default=False,
        ),
    ]