# Generated by Django 4.0.3 on 2022-10-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagne', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
