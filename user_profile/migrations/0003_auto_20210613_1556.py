# Generated by Django 3.0.8 on 2021-06-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20210613_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(blank=True, default='___', max_length=100, null=True),
        ),
    ]