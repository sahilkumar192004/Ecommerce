"""resource URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexpage,name='mainpage'),
    path('displaycource/<int:myid>',views.displaycource,name='displaycource'),
    path('displaycourcepaid/<int:myid>',views.displaycourcepaid,name='displaycourcepaid'),
    path('displaycource/myaddtocart',views.myaddtocart,name='myaddtocart'),
    path('mycart',views.mycart,name='mycart'),
    path('accordingtocato',views.accordingtocato,name="accordingtocato"),
    path('login',views.login,name="login"),
    path('createaccount',views.createaccount,name="createaccount"),
    path('logout',views.logout,name="logout"),
    path('changepassword2',views.changepassword2,name='changepassword2'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
     name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
        name="password_reset_complete"),
    path('contact',views.contact,name="contact"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('services',views.services,name="services"),
    path('events',views.events,name="events"),
    path('profile',views.profile,name="profile"),
    path('allcourses',views.allcourses,name="allcourses"),
    path('service1',views.service1,name="service1"),
    path('service2',views.service2,name="service2"),
    path('service3',views.service3,name="service3"),
    path('service4',views.service4,name="service4"),
    path('service5',views.service5,name="service5"),
    path('service6',views.service6,name="service6"),
    path('clearcart',views.clearcart,name='clearcart'),
    path('removecatitem',views.removecatitem,name='removecatitem'),
    path('courseprofile',views.courseprofile,name='courseprofile'),
    path('checkout',views.checkout,name='checkout'),
    path('orderdone',views.orderdone,name='orderdone'),
    path('verify_payment',views.verify_payment,name='verify_payment'),
    path('mycourcesdata',views.mycourcesdata,name='mycourcesdata'),
    path('search',views.search,name='search'),
    path('Latest_Happening_data/<int:myid>',views.Latest_Happening_data,name='Latest_Happening_data'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('refund_cancellation_policy',views.refund_cancellation_policy,name='refund_cancellation_policy'),
    path('Termsand_condition_policy',views.Termsand_condition_policy,name='Termsand_condition_policy'),
    path('particular_service/<int:myid>',views.particular_service,name='particular_service'),
]
