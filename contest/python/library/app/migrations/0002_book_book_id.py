# Generated by Django 3.0.5 on 2020-04-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(default=0),
        ),
    ]
