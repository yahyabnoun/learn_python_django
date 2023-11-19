from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , Http404
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


# def news_view(request,topic):
#     return HttpResponse(articles[topic])

# ----------------------------------------------------------------------------------------------

def sum_view(request,num1,num2):
    result = num1 + num2
    return HttpResponse(str(result))


# ----------------------------------------------------------------------------------------------

# def news_view(request,topic):
#     try:
#         return HttpResponse(articles[topic])
#     except:
#         result ="we don't have this topic"
#         return HttpResponseNotFound(result)
        

def news_view(request,topic):
    try:
        return HttpResponse(articles[topic])
    except:
        result ="we don't have this topic"
        raise Http404(result)