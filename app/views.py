from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from gem import settings
from app.templatetags.cart import total_cart_price ,price_total,cart_quantity
# Create your views here.
def indexpage(request):
    c=Product.objects.all()
    d=SizeVarient.objects.all()
    b=Category.objects.all()
    if "qry" in request.GET:
        q=request.GET['qry']
        if Product.objects.filter(select_category=q):
            c=Product.objects.filter(select_category=q)
            return render(request,'index.html',{'b':b,'c':c,'d':d})
    elif "yyy" in request.GET:
        q=request.GET['yyy']
        c=Product.objects.all()
        return render(request,'index.html',{'b':b,'c':c})
                

    return render(request,'index.html',{'b':b,'c':c,'d':d})

def indexpage2(request,myid):
    a=Product.objects.filter(id=myid)
    b=Product.objects.filter(select_category=myid)
    hi=Product.objects.get(id=myid)
    c=Category.objects.all()
    d=SizeVarient.objects.all()
    context={'a':a,'b':b,'c':c,'d':d}
    if request.GET.get('size'):
        size=request.GET.get('size')
        print(size)
        fun=SizeVarient.objects.get(size=size)
        price=int(fun.price) + int(hi.product_price)
        print(price)
        context['selected_size']=size
        context['updated_price']=price
        
    if request.method=="POST":
        prod=request.POST.get('productid')
        remove=request.POST.get('remove')
        print(prod)
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(prod)
            if quantity:
                if remove:
                    if quantity<=1:
                      cart.pop(prod)

                    else:
                       
                       cart[prod]=quantity-1
                else:

                  cart[prod]=quantity+1
            else:
                cart[prod]=1

        else:
            cart={}    
            cart[prod]=1
        request.session['cart']=cart
        print(request.session['cart'])

        
    
    return render(request,'product-details.html',context=context)

def product(request):
    a=Product.objects.all
    b=Category.objects.all()
    if "qry" in request.GET:
        q=request.GET['qry']
        print(q)
        if Product.objects.filter(select_category=q):
            a=Product.objects.filter(select_category=q)
        return render(request,'shop.html',{'a':a,'b':b})
    return render(request,'shop.html',{'a':a,'b':b})
def login(request):
    b=Category.objects.all()
    if request.method=="POST":
        usern=request.POST['username']
        passw=request.POST['password']
        user=auth.authenticate(username=usern,password=passw)
         
    return render(request,'client.html',{'b':b})
def signup(request):
    b=Category.objects.all()
    if request.method=="POST":
        fname=request.POST['fn']
        lname=request.POST['ln']
        pho=request.POST['phone']
        st=request.POST['street']
        ct=request.POST['city']
        cunt=request.POST['country']
        post=request.POST['postal']
        email=request.POST['email']
        usern=request.POST['username']
        passw=request.POST['pass']
        print(usern,passw)
        if User.objects.filter(username=usern).exists():
            messages.info(request,"Username already exist") 

        else:
            user=Userdetail.objects.create_user(username=usern,first_name=fname,last_name=lname,phone=pho,street=st,city=ct,country_name=cunt,pincode=post,email=email,password=passw)    
            user.save()
            user=auth.authenticate(username=usern,password=passw)
            if user is not None:
                print("yes")
                auth.login(request,user)
                if request.user.is_authenticated:
                    print("yes ")
                    return HttpResponseRedirect('/')
    return render(request,'signup.html',{'b':b})

def logout(request):
    request.session.clear()
    auth.logout(request)
    return redirect('/')


def b2b(request):
    if request.method=="POST":
        n=request.POST['Name']
        p=request.POST['phone']
        e=request.POST['Email']
        m=request.POST['Message']

        obj=B2b(name=n,phone=p,email=e,message=m)
        obj.save()
        return render(request,'index.html')

def contact(request):
    b=Category.objects.all()
    if request.method=='POST':
        n=request.POST['name']
        e=request.POST['email']
        m=request.POST['message']
        obj=Contact(name=n,email=e,message=m)
        obj.save()
    return render(request,'contact.html',{'b':b})

def cart(request):
       

            
        
            cart=request.session.get('cart')
            if not cart:
                request.session.cart={}
                return render(request,'shop-cart.html')

            ids=list(request.session.get('cart').keys())
            p=Product.objects.filter(id__in=ids)
            cart=request.session.get('cart')
            
            a=Product.objects.filter(id__in=list(cart.keys()))
            print(a)
            amount=total_cart_price(p,cart)
            print("amount is the ",amount)
       
        
            e=Category.objects.all()
            if 'size' in request.GET:
                size=request.GET.get('size')
                print("size is:",size)
                sizepri=SizeVarient.objects.get(size=size)
                sizea=SizeVarient.objects.all()
                context={'p':p,'e':e,'sizea':sizea,'sizepri':sizepri}
                pip=Product.objects.filter(id__in=ids)
                sum=0
                
                for i in pip:
                    print(i.product_name,"kaise ho app")
                    price=int(i.product_price)+int(sizepri.price)
                    pricet=cart_quantity(i,cart)*price
                    sum=sum+pricet
                    print("ramramji",pricet)
                    context['updated_price']=price
                    context['hello']=pricet
                    
                    context['ro']=sum
                

                return render(request,'shop-cart.html',context=context)
            return render(request,'shop-cart.html',{"p":p})

    # except:
    #     return render(request,'shop-cart.html')    

def checkout(request):
    if not request.user.is_authenticated:
        return render(request,'client.html')
    cart=request.session.get('cart')    
    ids=list(request.session.get('cart').keys())
    p=Product.objects.filter(id__in=ids)
    x=Product.objects.filter(id__in=list(cart.keys()))
    amount=total_cart_price(p,cart)
    profile=Userdetail.objects.get(user=request.user) 
    if request.method=="POST":
        n=request.POST['name']
        a=request.POST['num']
        b=request.POST['num1']
        c=request.POST['email']
        d=request.POST['add']
        for i in x:
            print("helo",cart.get(str(i.id)))
            order=Order(user=profile,userproduct=i,full_name=n,email=c,phone_no=a,alternate_no=b,address=d,price=i.product_price,quantity=cart.get(str(i.id)))
            order.save()
        html_content=render_to_string("email.html")
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
               "Your GOPALI Order confirmation",
                text_content,
                settings.EMAIL_HOST_USER,
                [c,'slanzapanikakri@gmail.com'],
                )
        email.attach_alternative(html_content,"text/html")
        email.send(fail_silently=False)
       
        return HttpResponse("we will contact u soon ")

    return render(request,'buy2.html')
def buy(request):
    if not request.user.is_authenticated:
        return render(request,'client.html')
    q=request.GET['qry']    
    pro=Product.objects.filter(id=q)
    e= Product.objects.get(id=q)
    x=e.product_price
    
    profile=Userdetail.objects.get(user=request.user) 
    if request.method=="POST":
        n=request.POST['name']
        a=request.POST['num']
        b=request.POST['num1']
        c=request.POST['email']
        d=request.POST['add']
        html_content=render_to_string("email.html")
        text_content=strip_tags(html_content)
        email=EmailMultiAlternatives(
               "Your GOPALI Order confirmation",
                text_content,
                settings.EMAIL_HOST_USER,
                [c,'slanzapanikakri@gmail.com'],
                )
        email.attach_alternative(html_content,"text/html")
        email.send(fail_silently=False)
        order=Order(user=profile,userproduct=e,full_name=n,email=c,phone_no=a,alternate_no=b,address=d,price=x)
        order.save()
        return HttpResponse("we will contact u soon ")
    return render(request,'buy.html',{'pro':pro})
        
def clearcart(request):
    if not request.user.is_authenticated:
        return render(request,'client.html')
    if request.user.is_authenticated:   
        request.session.clear()
        return redirect('/')

def remove(request):
   
    
    return render(request,'index.html')