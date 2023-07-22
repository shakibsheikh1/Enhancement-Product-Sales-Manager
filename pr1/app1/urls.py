from django.contrib import admin
from django.urls import path
from .views import hello, contact, signup,Loginviews,home,\
    searchview,about,datapost,Productview,Productdelete,Proall,z,zo,zoo,\
    logout,addprod,abouts,tome


urlpatterns = [
  #  path('admin/', admin.site.urls),
    path('index/', hello),
    path('contact/',contact,name='contact'),
    path("tome",tome,name='tome'),
    path('signup/',signup, name ='signup'),
    path('login/',Loginviews, name= 'Loginviews'),
    path('home/',home, name= 'home'),
    path('about/',about, name= 'about'),
    path('datapost/',datapost, name= 'datapost'),
    path('view/<int:abc>/',Productview,name='Productview'),
    path('del/<int:abc>/', Productdelete, name='Prodel'),

    path('Proall/',Proall,name= 'Proall'),
    # project files
    path('signto/',z,name = 'z'),
    path('loto/',zo,name= 'zo'),
    path('hom2/',zoo,name = 'zoo'),
    path('searchview/', searchview, name='searchview'),
    path('logout/',logout,name='logout'),
    path("addprod/",addprod,name='addprod'),
    path('abouts/',abouts, name='abouts')
]
