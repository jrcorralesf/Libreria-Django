# Generated by Django 3.2.3 on 2021-06-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20210602_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
