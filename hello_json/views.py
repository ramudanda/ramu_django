from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def json_msg(request):
    return JsonResponse({"Name": "Hello World!"})
