# Generated by Django 2.1.2 on 2018-10-28 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]