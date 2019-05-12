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


class SardanaFileUploadView(APIView):

    def put(self, request, pk):
        sardana = get_object_or_404(Sardana, pk=pk)
        serializer = SardanaSerializer(sardana, data={'file': request.FILES['file']}, partial=True)
        serializer.is_valid(raise_exception=True)
        sardana.file.delete()
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
