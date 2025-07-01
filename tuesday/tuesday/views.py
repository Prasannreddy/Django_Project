from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
def About_Page(request):
    return HttpResponse("Hello Django")
def Shopping_Page(request):
    data={"city":"Hyderabad"}
    return HttpResponse("Welcome to Shopping")
# html page
def showing_html(request):
    return render(request,"home.html")