# Generated by Django 4.1.3 on 2022-12-31 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_cooperationducument_responsible_approval_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperationducument',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cooperationducument',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
