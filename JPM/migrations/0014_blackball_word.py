# Generated by Django 2.2.6 on 2022-06-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPM', '0013_blackball_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackball',
            name='word',
            field=models.BooleanField(default=False),
        ),
    ]