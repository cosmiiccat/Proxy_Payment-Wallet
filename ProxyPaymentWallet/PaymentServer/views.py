from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from utils import custom_exceptions
from django.http import JsonResponse

from rest_framework.decorators import api_view

import json
import os


# Create your views here.
@api_view(['GET'])
def ensure(request):
    try:
        if request.method != "GET":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        return JsonResponse({"success": "true", "status": "online"}) 
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})




@api_view(['POST'])
@csrf_exempt 
def reverse_internet_search(request):
    try:
        if request.method != "POST":
            raise custom_exceptions.CustomError(f"Method - {request.method} is not Allowed")
        
        req_data = json.loads(request.body.decode('utf-8'))
        for key in ["type", "image"]:
            if key not in req_data.keys():
                raise custom_exceptions.CustomError(f"The parameter {key} in JSON Body is missing")

        resp = {}
        return JsonResponse({"success": "true", "data": resp}) 
    
    except Exception as e:
        return JsonResponse({"success":"false", "error":f"{e}"})