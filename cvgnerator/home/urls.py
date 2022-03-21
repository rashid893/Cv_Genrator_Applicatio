import imp
from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
 path('',views.index,name="index"),
  path('<int:id>/',views.resume,name="resume"),
  path('list/',views.list,name='list'),
]
