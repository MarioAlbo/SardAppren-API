from rest_framework import serializers

from sardanas.models import Sardana


class SardanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sardana
        fields = '__all__'
