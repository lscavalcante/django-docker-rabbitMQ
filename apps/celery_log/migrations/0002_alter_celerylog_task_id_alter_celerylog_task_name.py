# Generated by Django 4.2 on 2023-04-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celerylog',
            name='task_id',
            field=models.CharField(editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='celerylog',
            name='task_name',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]