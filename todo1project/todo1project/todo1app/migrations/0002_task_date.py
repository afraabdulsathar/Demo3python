# Generated by Django 4.2.2 on 2023-07-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo1app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-22'),
            preserve_default=False,
        ),
    ]
