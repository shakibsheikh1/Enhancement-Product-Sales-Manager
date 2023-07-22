from django.contrib import admin
from  .models import Product,Signup,Blog,Author,Entry,Pro
# Register your models here.
admin.site.register(Product)
admin.site.register(Signup)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Entry)
class Proadmin(admin.ModelAdmin):
    list_display = ['name','des','price','img','review']
    list_filter = ['name','des','price','img','review']
admin.site.register(Pro,Proadmin)

admin.site.site_header = 'My Project'
admin.site.site_title  = 'SiteName you'
admin.site.index_title   = 'Admin you'