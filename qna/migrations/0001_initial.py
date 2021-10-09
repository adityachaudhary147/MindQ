# Generated by Django 3.0.8 on 2021-06-11 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('url', django_mysql.models.ListTextField(models.CharField(blank=True, max_length=300), blank=True, default='', size=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default='set-some-slug-bro', max_length=300)),
                ('downvote', models.ManyToManyField(related_name='QDownVote', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='QTag', to='qna.Tag')),
                ('upvote', models.ManyToManyField(related_name='QUpVote', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='QUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerQ',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('url', django_mysql.models.ListTextField(models.CharField(blank=True, max_length=300), blank=True, default='', null=True, size=10)),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='qna.AnswerQ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='QAnswere', to='qna.Question')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]