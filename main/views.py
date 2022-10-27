from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .models import SlackPerson
from .serializers import SlackPersonSerializer

# Create your views here.
@csrf_exempt
def person_list(request):
    if request.method == 'GET':
        people = SlackPerson.objects.all()
        serializer = SlackPersonSerializer(people, many=True)
        return JsonResponse(serializer.data, safe=False)