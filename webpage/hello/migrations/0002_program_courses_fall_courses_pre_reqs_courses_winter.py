# Generated by Django 4.1.3 on 2022-11-19 19:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='fall',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courses',
            name='pre_reqs',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), default=list, size=8), default=list, size=8),
        ),
        migrations.AddField(
            model_name='courses',
            name='winter',
            field=models.BooleanField(default=False),
        ),
    ]
