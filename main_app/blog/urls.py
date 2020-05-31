from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>',views.post_details,name='post_details'),
    path('tags=<slug:tag>',views.post_by_tag,name='post_by_tag'),
    path('categery=<slug:categery>',views.post_by_categery,name='post_by_categery'),

]