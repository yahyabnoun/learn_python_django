from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# ----------------------------------------------------------------------------------------------

# def sports_view(request):
#     return HttpResponse("sports page")

# def finance_view(request):
#     return HttpResponse("finance page")

# ----------------------------------------------------------------------------------------------

articles = {
    'sports':"sports page",
    'finance':"finance page",
    'politics':"politics page",
}


def news_view(request,topic):
    return HttpResponse(articles[topic])

# ----------------------------------------------------------------------------------------------

def sum_view(request,num1,num2):
    result = num1 + num2
    return HttpResponse(str(result))