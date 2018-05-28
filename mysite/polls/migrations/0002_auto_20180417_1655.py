# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=200)),
                ('Second_Name', models.CharField(max_length=200)),
                ('Age', models.IntegerField(max_length=200)),
                ('Country', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Proffession', models.CharField(max_length=200)),
                ('occupation', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]