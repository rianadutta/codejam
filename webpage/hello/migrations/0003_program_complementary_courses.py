# Generated by Django 4.1.3 on 2022-11-20 00:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_program_courses_fall_courses_pre_reqs_courses_winter'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='complementary_courses',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), default=list, size=8), default=list, size=8),
        ),
    ]
