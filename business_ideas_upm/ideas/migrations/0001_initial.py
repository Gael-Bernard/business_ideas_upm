# Generated by Django 4.1.3 on 2022-11-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=128)),
                ('body', models.TextField(max_length=4096)),
                ('username', models.TextField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='IdeaComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=128)),
                ('body', models.TextField(max_length=4096)),
                ('username', models.TextField(max_length=32)),
            ],
        ),
    ]
