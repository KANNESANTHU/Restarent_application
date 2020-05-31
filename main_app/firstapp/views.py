from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from . import models

#from firstapp import models
from blog.models import Post
from aboutus.models import Why_choose_us
# Create your views here.
def meal_list(request):
    meallist=models.Meal.objects.all()

    categeries = models.Categery.objects.all()

    context={'meal_list':meallist,
             'categeries':categeries,
             }
    return render(request,'meals/index.html', context)
def meal_details(request,id):
    meal_detail=models.Meal.objects.get(id=id)
    context={'meal_details':meal_detail}
    return render(request,'meals/details.html', context)

def index(request):
    return render(request, 'firstapp/index.html')
def login(request):
    return render(request, 'firstapp/login.html')

def register(request):
    return render(request,'firstapp/register.html')

def reg_done(request):

    regobj=models.Register()

    name=request.POST.get('user_name')
    email=request.POST.get('user_email')
    phone=request.POST.get('user_phone')
    psw=request.POST.get('user_password')
    pswr=request.POST.get('rpsw')

    regobj.name=name
    regobj.email=email
    regobj.phone=phone
    regobj.psw=psw
    regobj.pswr=pswr
    regobj.save()

    return render(request, 'firstapp/login.html')
def login_done(request):
    #obj=models.Register()
    email=request.POST.get('user_email')
    pword=request.POST.get('user_password')

    #mail=obj.email
    #pw=obj.psw
    for i in models.Register.objects.all():
        if i.email==email and i.psw==pword:
            meals = models.Meal.objects.all()
            meallist = models.Meal.objects.all()
            why_choose_us = Why_choose_us.objects.all()
            categeries = models.Categery.objects.all()
            posts = Post.objects.all()
            latest_post = Post.objects.last()
            context = {
                'meals': meals,
                'meal_list': meallist,
                'categeries': categeries,
                'posts': posts,
                'latest_post': latest_post,
                'why_choose_us': why_choose_us,
            }
            return render(request,'home/index.html',context)

    return redirect(reverse('login'))