from django.urls import path
from restaurent_app2 import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),    
    path('contactus1',views.contactus1,name='contactus1'),
    path('menu',views.menu,name='menu'),    
    path('menu1',views.menu1,name='menu1'),
    path('blog',views.blog,name='blog'),
    path('blog_detail',views.blog_detail,name='blog_detail'),
    path('menu_detail',views.menu_detail,name='menu_detail'),
    path('login',views.login,name='login'),
    path('cart',views.cart,name='cart'),
    path('home_page1',views.home_page1,name='home_page1'),    
    path('aboutus1',views.aboutus1,name='aboutus1'),






    
]