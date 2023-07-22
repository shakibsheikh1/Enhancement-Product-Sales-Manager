from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import Signup,Product,Pro
from django.db.models import Q

# Create your views here.
def hello(request):
    a=Signup.objects.all()
    return render(request,'index.html',{'q':a})
def contact(request):
    return render(request,'contact.html')
def tome(request):
    return render(request,'tome.html')
def signup(request):
    if request.method == 'POST':
        a=Signup()
        a.Email= request.POST['Email']
        a.Mobile_No= request.POST['number']
        a.Name = request.POST['username']
        a.Password= request.POST['Password']
        a.save()
    return render(request,'signup.html')
def login(request):
    a="hello"
    b= 12*4
    return render(request,'Loginviews.html',{'q':a,'w':b})
def home(request):
    return render(request,'home.html')
def about(request):
    # s = searchview(request)
    return render(request,'about.html')
def datapost(request):
    if request.method == 'POST':
        model= Product()
        model.name= request.POST['user-name']
        model.email= request.POST['email']
        model.save()
    return render(request,'datapost.html')
def Productview(request,abc):
    v=Pro.objects.get(id=abc)
    return render(request,'Productview.html',{'v':v})
def Productdelete(request,abc): 
    v=Pro.objects.get(id=abc)
    v.delete()
    return redirect('Proall')
def Proall(request):
    if 'xyz' in request.session.keys():
           l =Pro.objects.all()

           return render(request,'Proall.html',{'l':l})
    else:
        return redirect('Loginviews')
#     q = request.GET.get('Search')
#     if q:
#         pr = Pro.objects.filter(Q(name__icontains=q) | Q(price__icontains=q))
#         data = {'p': pr}
#     else:
#         data = {}
#         # return data
#     return render(request, 'Proall.html', data)
def Loginviews(request):
    if request.method == 'POST':
        try:
            print("123")
            m = Signup.objects.get(Email=request.POST['email'])
            print(m)
            if m.Password == request.POST['pass']:
                request.session['xyz']=m.id
                print("pass")
                return redirect('Proall')
            else:
                return HttpResponse("wrong password")
        except:
            return HttpResponse("wrong email")
    return render(request, 'Loginviews.html')

                  # project files
def z(request):
    return render(request,'z-signup.html')
def zo(request):
    return render(request,'login_z.html')
def zoo(request):
    return render(request,'hom2.html')
def searchview(request):
   q = request.GET.get('search')
   # another way
   # try:
   #    q = request.GET.get('search')
   # except:
   #     q = None
   if q:
       pr = Pro.objects.filter(Q(name__icontains=q) | Q(price__icontains=q))
       data = {'p':pr}
   else:
       data= {}
       # return data
   return render(request,'Proall.html',data)
def logout(request):
    if 'xyz' in request.session.keys():
        del request.session['xyz']
        return redirect('Loginviews')
    else:
        return redirect('Loginviews')
def addprod(request):
    if request.method  == 'POST':
        b = Pro()
        b.name = request.POST['name']
        b.des = request.POST['des']
        if (request.FILES)!=0:
           b.img = request.FILES['img']
        b.price = request.POST['price']
        b.review = request.POST['review']
        b.save()
    return render(request,'addprod.html')
def abouts(request):
    return render(request,'abouts.html')
