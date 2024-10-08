from rest_framework.serializers import ModelSerializer
from .models import Student,Imagepload

class Studentserializer(ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"


class ImageSerializer(ModelSerializer):
    class Meta:
        model=Imagepload
        fields="__all__"  
