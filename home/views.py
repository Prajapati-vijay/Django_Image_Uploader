from django.shortcuts import render
from .serializer import Studentserializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student,Imagepload
from rest_framework.serializers import Serializer
from .serializer import ImageSerializer
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

@api_view(['GET'])
def Home(request):
    res=Student.objects.all()
    data=Studentserializer(res,many=True)
    return Response(data.data)



class ImageViewset(ModelViewSet):
    queryset = Imagepload.objects.all()
    serializer_class = ImageSerializer
   
    


