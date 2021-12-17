from core.models import Door
from rest_framework import serializers


class DoorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Door
        fields = ('id', 'name', 'status')
        read_only_fields = ('id', )

    