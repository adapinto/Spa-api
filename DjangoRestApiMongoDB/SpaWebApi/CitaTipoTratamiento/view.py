from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from SpaWebApi.models import CitaTipoTratamiento, Cita, TipoTratamiento
from SpaWebApi.serializers import CitaTipoTratamientoSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def citaTipoTratamiento_list(request):
    if request.method == 'GET':
        citaTipoTratamiento = CitaTipoTratamiento.objects.all()
        citaTipoTratamiento_serializer = CitaTipoTratamientoSerializer(citaTipoTratamiento, many=True)
        return JsonResponse(citaTipoTratamiento_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        citaTipoTratamiento_data = JSONParser().parse(request)
        citaTipoTratamiento_serializer = CitaTipoTratamientoSerializer(data=citaTipoTratamiento_data)
        if citaTipoTratamiento_serializer.is_valid():
            citaTipoTratamiento_serializer.save()
            return JsonResponse(citaTipoTratamiento_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(citaTipoTratamiento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)