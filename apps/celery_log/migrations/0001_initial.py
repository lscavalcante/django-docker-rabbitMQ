# Generated by Django 4.2 on 2023-04-09 23:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=50)),
                ('task_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_executed', models.DateTimeField(blank=True, null=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('traceback', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
