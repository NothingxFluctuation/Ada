# Generated by Django 2.2.6 on 2022-06-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JPM', '0008_auto_20220620_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='cp',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=10),
        ),
    ]
