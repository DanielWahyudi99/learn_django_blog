
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import blogviewset ,matematikaviewset

from . import views
router = routers.DefaultRouter()
#router.register(r"api-blog",blogviewset)
router.register(r"blog",blogviewset)
router.register(r"matematika",matematikaviewset)
urlpatterns = [
    #path('',views.index,name='indexku'),#slash blog

    path('', include (router.urls)),#slash blog
    #path('matematika/',views.index,name='indexku'),
    path('first-site',views.firstpage,name='firstsite'),
    path('addblog',views.addblogviewsku,name='addblognameku'), # name itu alias sebelahnya yang kiri harus sama dengan url
    path('update/<int:idnya>',views.updatepageviewsku,name='updatepageku'), #/<int:id> ini untuk menunjukan kalau dinamis dan hanya value integer
    path('updateaction/<int:idnya>', views.updatepageactionviewsku, name='updateactionpageku'),
    path('delete/<int:idnya>',views.deleteactionviewsku, name='deleteactionpageku'),


]
