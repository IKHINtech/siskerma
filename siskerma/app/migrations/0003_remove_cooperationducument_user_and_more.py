# Generated by Django 4.1.3 on 2022-12-06 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cooperationducument_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cooperationducument',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='cooperation_document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cooperationducument'),
        ),
    ]
