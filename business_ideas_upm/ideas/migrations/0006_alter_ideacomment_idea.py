# Generated by Django 4.1.3 on 2022-11-18 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0005_ideacomment_idea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideacomment',
            name='idea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.businessidea'),
        ),
    ]