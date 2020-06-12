from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	return HttpResponse("Python_ecommerce_Homepage_Lakmal")
def about_page(request):
    return HttpResponse("About page")
def contact_page(request):
    return HttpResponse("Contact page")
