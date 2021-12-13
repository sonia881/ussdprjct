# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

def welcome (request):
    return HttpResponse('Welcome to our web api')

@csrf_exempt
def Farmers(request):
    if request.method =='GET':
        FarmersData= Farmers.objects.all()
        serializer =FarmersSerializer(FarmersData, many=True)
        return JsonResponse(serializer.data, status=200, safe=)
    
    elif request.mathod =='POST':
        data =JSONParser().parse(request)
        serializer = FarmersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def farmersUpdate(request, id):
    if request.method == 'GET':
        farmerData = Farmers.objects.get(id=id)
        serializer = FarmersSerializer(farmerData, many=False)
        return JsonResponse(serializer.data, status=200, safe=False)
    elif request.method =='PUT':
        data = JSONParser().parse(request)

        farmerData = Farmers.objects.get(id=id)
        farmerData.fullname = data['fullname']
        farmerData.email = data['email']
        farmerData.phone = data['phone']
        farmerData.save()
        serializer = FarmersSerializer(farmerData)

        return JsonResponse(serializer.data, status=201)
    elif request.method == 'DELETE':
        farmerData = Farmers.objects.get(id=id).delete()
        serializer = FarmersSerializer(farmerData, many=False)
        return JsonResponse('Data has been deleted', status=200, safe=False)

            


