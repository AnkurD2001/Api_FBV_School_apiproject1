from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
#@api_view(['GET','POST','DELETE','UPDATE'])
@permission_classes([IsAuthenticated])
def schoolJsonData(request):
    SOD=School.objects.all()
    JOD=SchoolaModelSerializer(SOD,many=True)
    jsondata=JOD.data
    return Response(jsondata)












