from django.shortcuts import render
#from main_app.firstapp.models import Meal
#from main_app.firstapp.models import Meal
from firstapp import models
from blog.models import Post
from aboutus.models import Why_choose_us
def home(request):
    meals=models.Meal.objects.all()
    meallist = models.Meal.objects.all()
    why_choose_us = Why_choose_us.objects.all()
    categeries = models.Categery.objects.all()
    posts=Post.objects.all()
    latest_post=Post.objects.last()
    context={
        'meals':meals,
        'meal_list':meallist,
        'categeries':categeries,
        'posts':posts,
        'latest_post':latest_post,
        'why_choose_us': why_choose_us,
    }

    return render(request,'home/index.html',context)