from rest_framework import serializers
from .models import *

class Jobs_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields='__all__'
