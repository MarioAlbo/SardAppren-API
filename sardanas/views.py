import os

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from sardanas.models import Sardana
from sardanas.serializer import SardanaSerializer


class SardanesList(ListCreateAPIView):
    queryset = Sardana.objects.all()
    serializer_class = SardanaSerializer


class SardanaDetail(RetrieveAPIView):
    queryset = Sardana.objects.all()
    serializer_class = SardanaSerializer


class SardanaFileView(APIView):

    def get(self, request, pk):
        sardana = get_object_or_404(Sardana, pk=pk)

        file_path = os.path.join(settings.MEDIA_ROOT, sardana.file.name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read())
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        raise Http404

    def put(self, request, pk):
        sardana = get_object_or_404(Sardana, pk=pk)
        serializer = SardanaSerializer(sardana, data={'file': request.FILES['file']}, partial=True)
        serializer.is_valid(raise_exception=True)
        sardana.file.delete()
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
