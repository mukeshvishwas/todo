# Generated by Django 4.1.10 on 2023-08-23 10:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=250)),
                ('slot', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
