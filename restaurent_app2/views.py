from django.shortcuts import render,redirect


# Create your views here.
def home_page(request):
    return render(request,'home.html')

def home_page1(request):
    return render(request,'home1.html')

def aboutus(request):
    return render(request,'about.html')

def aboutus1(request):
    return render(request,'about1.html')

def contactus(request):
    return render(request,'contact.html')

def contactus1(request):
    return render(request,'contact1.html')

def menu(request):
    return render(request,'menu.html')

def menu1(request):
    return render(request,'menu1.html')

def blog(request):
    return render(request,'blog.html')

def blog1(request):
    return render(request,'blog1.html')

def blog_detail(request):
    return render(request,'blog_detail.html')

def menu_detail(request):
    return render(request,'menu_detail.html')

def menu_detail1(request):
    return render(request,'menu_detail1.html')

def login(request):
    return render(request,'login.html')

def cart(request):
    return render(request,'cart.html')
