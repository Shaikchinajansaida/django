from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def sample(request):
    return HttpResponse("Hello")
def sample1(requst):
    return HttpResponse("welcome to django")
def sampleinfo(requst):
    data ={"result":[1,2,3]}
    return JsonResponse(data)
def dynamicResponse(request):
    name=request.GET.get("name","jansaida")
    city=request.GET.get("city","hyd")
    return HttpResponse(f"hello {name} from {city}")
