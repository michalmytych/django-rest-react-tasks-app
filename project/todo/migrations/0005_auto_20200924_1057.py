# Generated by Django 3.1.1 on 2020-09-24 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_projecttodo_is_default_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thingtodo',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='todo.projecttodo'),
        ),
    ]