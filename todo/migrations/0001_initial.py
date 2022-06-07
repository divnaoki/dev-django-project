# Generated by Django 4.0.4 on 2022-06-05 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2022, 6, 5, 2, 33, 4, 947191))),
                ('update_time', models.DateTimeField(default=datetime.datetime(2022, 6, 5, 2, 33, 4, 947227))),
                ('limit_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
