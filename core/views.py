from django.shortcuts import render

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Door
from core.serializers import DoorSerializer


class DoorDetailView(APIView):
    serializer_class = DoorSerializer
    def get(self, request, id):
        door = Door.objects.get(pk=id)
        serializer = self.serializer_class(door)
        return Response(serializer.data)
