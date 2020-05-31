from django.shortcuts import render
from .models import Aboutus,Why_choose_us,Chef

def aboutus_list(request):
    about=Aboutus.objects.last()
    why_choose_us=Why_choose_us.objects.all()
    chef=Chef.objects.all()

    context={'about':about,
             'why_choose_us':why_choose_us,
             'chef':chef,

    }
    return render(request,'aboutus/about.html',context)

# Create your views here.
