from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveAPIView
from rest_framework.response import Response

from sardanas.models import Sardana
from sardanas.serializer import SardanaSerializer


class SardanesList(ListCreateAPIView):
    queryset = Sardana.objects.all()
    serializer_class = SardanaSerializer


class SardanaDetail(RetrieveAPIView):
    queryset = Sardana.objects.all()
    serializer_class = SardanaSerializer
