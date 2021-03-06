# Generated by Django 3.0.8 on 2021-06-11 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('job', models.CharField(blank=True, max_length=100, null=True)),
                ('account_created', models.DateField(auto_now_add=True)),
                ('profile_image', models.ImageField(default='user_profile/default_profile2.png', upload_to='user_profile')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
