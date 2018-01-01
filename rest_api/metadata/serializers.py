# -*- coding:utf-8 -*-
from rest_framework import serializers
from models import *
# from django.contrib.auth.models import User

class LayerSerializer(serializers.HyperlinkedModelSerializer):
    last_updated_by = serializers.ReadOnlyField(source='last_updated_by.username')

    class Meta:
        model = Layer
        fields = ('url', 'last_updated_ts', 'last_updated_by', 'name', 'desc','system')

class SystemSerializer(serializers.ModelSerializer):
    last_updated_by = serializers.ReadOnlyField(source='last_updated_by.username')
    # layers = serializers.HyperlinkedRelatedField(many=True,
    #                                              view_name='layer-detail',
    #                                              queryset=Layer.objects.all())
    layers = LayerSerializer(many=True,read_only=True)

    class Meta:
        model = System
        fields = ('url', 'last_updated_ts', 'last_updated_by', 'name', 'desc', 'layers')