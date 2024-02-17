from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('link/', KitLink.as_view()),
    path('image/',KitImage.as_view()),
    path('create/',createKitView.as_view()),
    path('getAll/',getAllKitView.as_view()),
    path('<int:kitId>/',deleteKitView.as_view()),
    path('getMetaData/',getMetaData.as_view()),

]