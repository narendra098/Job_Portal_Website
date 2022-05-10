import json
from logging.handlers import DatagramHandler
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import *
from rest_framework.decorators import api_view

    
class PostJob(CreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = Jobs_Serializer


class ViewJobs(ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = Jobs_Serializer

class JobRetrive(RetrieveAPIView):
    queryset = Jobs.objects.all()
    serializer_class = Jobs_Serializer

class UpdateJob(RetrieveUpdateAPIView):
    queryset = Jobs.objects.filter()
    serializer_class = Jobs_Serializer