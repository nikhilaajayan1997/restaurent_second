from django.urls import path
from restaurent_app2 import views

urlpatterns=[
    path('',views.home_page,name='home_page'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('menu',views.menu,name='menu'),
    path('blog',views.blog,name='blog'),
    path('blog_detail',views.blog_detail,name='blog_detail'),
    path('menu_detail',views.menu_detail,name='menu_detail'),
    path('login',views.login,name='login'),




    
]