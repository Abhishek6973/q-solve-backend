from django.urls import path
from .views import *

urlpatterns = [
    path('getAll/', getAllQuestions.as_view()),

]