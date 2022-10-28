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
    if request.method == 'GET':
        people = SlackPerson.objects.all()
        serializer = SlackPersonSerializer(people, many=True)
        return JsonResponse(serializer.data, safe=False, headers=header)


# from rest_framework.decorators import api_view
# from django.http import JsonResponse
# @api_view(["GET"])
# def home(request, *args, **kwargs):
#   header = {"Access-Control-Allow-Origin":"*"}
#   data = {
#     "slackUsername":"",
#     "backend":True,
#     "age": yourage,
#     "bio":"your bio"
#   }
#   return JsonResponse(data,headers=header)