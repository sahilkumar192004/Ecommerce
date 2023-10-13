from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Product(models.Model):
    select_category=models.ForeignKey(Category,on_delete=models.CASCADE,default=0)
    product_image1=models.ImageField(upload_to="gallery")
    product_image2=models.ImageField(upload_to="gallery")
    product_image3=models.ImageField(upload_to="gallery")
    product_image4=models.ImageField(upload_to="gallery")
    product_name=models.CharField(max_length=200)
    product_price=models.IntegerField(default=0)
    product_offer=models.IntegerField(default=0)
    product_description=RichTextField()



    def __str__(self):
        return self.product_name


class SizeVarient(models.Model):
    size=models.CharField(max_length=10)
    price=models.CharField(max_length=20)

    def __str__(self) :
        return self.size +" "+ self.price


class Offerzone(models.Model):
    select=models.ForeignKey(Product,on_delete=models.CASCADE)        

    def __str__(self):
        return self.select
class Feedbacks(models.Model):
    select_c=models.ForeignKey(Product,on_delete=models.CASCADE)    
    name=models.CharField(max_length=200)
    review=models.TextField()
    
class Userdetail(User):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,parent_link=True)    
    phone=models.CharField(max_length=10)
    alternate_number=models.CharField(max_length=10)
    country_name=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    pincode=models.CharField(max_length=500)
    street=models.CharField(max_length=500)

  
    
class B2b(models.Model):
    name=models.CharField(max_length=200)
    phone=models.IntegerField(default=0)
    email=models.CharField(max_length=300)
    message=models.TextField()

    def __str__(self) -> str:
        return self.name +" "+ self.email

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    message=models.TextField()

    def __str__(self):
        return self.name+ " " +self.email


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    userproduct=models.ForeignKey(Product,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    quantity=models.IntegerField(default=1)
    phone_no=models.IntegerField(default=0,max_length=10)
    alternate_no=models.IntegerField(default=0,max_length=10)
    price=models.CharField(max_length=100)
    address=models.TextField()
    status=models.BooleanField(default=True)
    date=models.DateTimeField(auto_now_add=True)
     