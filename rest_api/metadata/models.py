# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

def set_default_columns(model_name):
    return_list=[]
    return_list.append(models.DateTimeField(auto_now_add=True))
    return_list.append(models.DateTimeField(auto_now=True))
    return_list.append(models.ForeignKey('auth.User', related_name=model_name))
    return return_list

class System(models.Model):
    created ,last_updated_ts ,last_updated_by = set_default_columns('systems')
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=60)
    class Meta:
        ordering = ('created',)

class Tablespace(models.Model):
    created, last_updated_ts, last_updated_by = set_default_columns('tablespaces')
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=60)
    class Meta:
        ordering = ('created',)

class Layer(models.Model):
    created, last_updated_ts, last_updated_by = set_default_columns('layers')
    system = models.ForeignKey(System,related_name='systems')
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=60)
    class Meta:
        ordering = ('created',)

class Table(models.Model):
    created, last_updated_ts, last_updated_by = set_default_columns('tables')
    layer= models.ForeignKey(Layer,related_name='layers',null=True)
    tablespace = models.ForeignKey(Tablespace,related_name='tablespaces',null=True)
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=60)
    class Meta:
        ordering = ('created',)