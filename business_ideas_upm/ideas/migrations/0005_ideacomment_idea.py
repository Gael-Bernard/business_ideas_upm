# Generated by Django 4.1.3 on 2022-11-18 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_alter_businessidea_publish_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideacomment',
            name='idea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ideas.businessidea'),
        ),
    ]
