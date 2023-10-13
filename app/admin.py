from django.contrib import admin
from .models import *
# Register your models here.
class AAdmin(admin.TabularInline):
    model=Feedbacks
class PAdmin(admin.ModelAdmin):
    inlines=[AAdmin]    
admin.site.register(Category)
admin.site.register(Product,PAdmin)
admin.site.register(Offerzone)
admin.site.register(Feedbacks)
admin.site.register(Userdetail)
admin.site.register(B2b)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(SizeVarient)
