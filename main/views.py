from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .models import SlackPerson
from .serializers import SlackPersonSerializer

# Create your views here.
@csrf_exempt
def person_list(request):
    header = {"Access-Control-Allow-Origin":"*"}
    data = {
    "slackUsername":"fife",
    "backend":True,
    "age": 19,
    "bio":"I am an undergraduate, studying Computer Science, I am an up and coming Django developer"
  }
    return JsonResponse(data, safe=False, headers=header)