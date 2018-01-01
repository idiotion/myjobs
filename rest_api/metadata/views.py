# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render
from models import System
from serializers import *
from permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework import permissions ,viewsets,filters

from rest_framework.response import Response
from rest_framework.decorators import detail_route
# from rest_framework import renderers
# Create your views here.
class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filter_fields = ('name',)
    search_fields = ('name','desc')

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user)

class LayerViewSet(viewsets.ModelViewSet):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    filter_fields = ('name','system')
    search_fields = ('name','desc')

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user)

# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer