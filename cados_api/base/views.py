from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Advocat
# Create your views here.

@api_view(['GET'])
def endpionts(request):
    data = ['/advocates','/advocates/:username']
    return Response(data)
 

def advocate_list(request):
    advocates = Advocat.objects.all()
    return Response(advocates)


def advocate_detail(request, username):
    data = username
    return Response(data )    