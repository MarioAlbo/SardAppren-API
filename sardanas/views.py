
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from sardanas.models import Sardana
from sardanas.serializer import SardanaSerializer


class SardanesList(ListCreateAPIView):
    queryset = Sardana.objects.all()
    serializer_class = SardanaSerializer


# @api_view(['GET'])
# def sardana_detail(request, sardana_id):
#     try:
#         sardana = Sardana.objects.get(id=sardana_id)
#     except Sardana.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = SardanaSerializer(sardana)
#         return Response(serializer.data)
#
#
