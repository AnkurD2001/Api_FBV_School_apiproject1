from rest_framework import serializers
from app.models import *

class SchoolaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'
        #fields=['Scname','Sclocation']