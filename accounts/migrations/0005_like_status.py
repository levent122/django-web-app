# Generated by Django 2.1.2 on 2018-10-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_like_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
