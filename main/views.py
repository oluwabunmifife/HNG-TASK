
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .models import SlackPerson
from .serializers import SlackPersonSerializer
from rest_framework.decorators import api_view
import random

#openai imports

import openai

openai.api_key = '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'
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



@api_view(['POST'])
def mathoperation(request):
    header = {"Access-Control-Allow-Origin":"*"}
    data = request.data
    result = 0
    Addarr = ['add', 'sum', 'addition', 'plus', 'sum of', 'add up', 'adding', 'addition of', 'sumation', 'summing']
    Diffarr = ['subtract', 'difference', 'minus', 'subtraction', 'difference of', 'subtracting', 'subtracted', 'subtraction of', 'minusing']
    Multarr = ['multiply', 'times', 'product', 'multiplication', 'product of', 'multiplicating', 'multiplying', 'multiplied', 'multiplication of']
    
    x = int(data['x'])
    y = int(data['y'])

    operation = str(data['operation_type'])
    operations = operation.split(" ")
    for i in operations:
      if i.lower() in Addarr:
        result = x + y
        operation = "addition"
        break
      elif i.lower() in Diffarr:
        result = x - y
        operation = "subtraction"
        break
      elif i.lower() in Multarr:
        result = x * y
        operation = "multiplication"
        break
      else:
        operation = "Invalid Operation"
        
      
        

    # prompt = data['prompt']

    # if operation == 'add':
    #     result = x + y
    # elif operation == 'subtract':
    #     result = x - y
    # elif operation == 'multiply':
    #     result = x * y
    # else:
    #   result = "Invalid operation"

  #   response = openai.Completion.create(
  #   model="text-davinci-001",
  #   prompt=operation,
  #   temperature=0,
  #   max_tokens=100,
  #   top_p=1,
  #   frequency_penalty=0.2,
  #   presence_penalty=0
  # )
    new_data = {

          "slackUsername":"fife",
          "x": x,
          "y": y,
          "operation_type": operation,
          "result": result
      }
    
    #openapi stuff
    
    return Response(new_data, status=status.HTTP_200_OK, headers=header)





#   data = request.data
#   x = data['x']
#   y = data['y']
#   operation_type = data['operation_type']
#   prompt = data['prompt']

#   #openapi stuff
#   response = openai.Completion.create(
#   model="text-davinci-001",
#   prompt=prompt,
#   temperature=0,
#   max_tokens=100,
#   top_p=1,
#   frequency_penalty=0.2,
#   presence_penalty=0
# )

#   print(response)

