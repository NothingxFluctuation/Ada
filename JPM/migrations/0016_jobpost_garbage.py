# Generated by Django 2.2.6 on 2022-06-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPM', '0015_jobpost_same_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='garbage',
            field=models.BooleanField(default=False),
        ),
    ]
