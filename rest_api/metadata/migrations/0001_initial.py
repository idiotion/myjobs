# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 13:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated_ts', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=60)),
                ('last_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated_ts', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=60)),
                ('last_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='systems', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated_ts', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=60)),
                ('last_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tables', to=settings.AUTH_USER_MODEL)),
                ('layer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layers', to='metadata.Layer')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Tablespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated_ts', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32)),
                ('desc', models.CharField(max_length=60)),
                ('last_updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablespaces', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='table',
            name='tablespace',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tablespaces', to='metadata.Tablespace'),
        ),
        migrations.AddField(
            model_name='layer',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='systems', to='metadata.System'),
        ),
    ]
