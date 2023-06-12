from django.shortcuts import render,redirect


# Create your views here.
def home_page(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

def blog(request):
    return render(request,'blog.html')

def blog_detail(request):
    return render(request,'blog_detail.html')

def menu_detail(request):
    return render(request,'menu_detail.html')

def login(request):
    return render(request,'login.html')
