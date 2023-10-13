from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('indexpage2/<int:myid>',views.indexpage2,name='indexpage2'),
path('login',views.login,name='login'),
path('signup',views.signup,name='signup'),
path('logout',views.logout,name='logout'),
path('b2b',views.b2b,name="b2b"),
path('product',views.product,name="product"),
path('contact',views.contact,name="contact"),
path('cart',views.cart,name="cart"),
path('buy',views.buy,name="buy"),
path('clearcart',views.clearcart,name="clearcart"),
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
path('checkout',views.checkout,name="checkout"),

]