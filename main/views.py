from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request): 
    
    return HttpResponse('Hello world')


from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def read_json(request): 
    if request.method == 'POST': 
        payload = json.loads(request.body)
        print(payload[0])
        return HttpResponse('data sent')

    return HttpResponse('Read Json')

