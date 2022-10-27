from django.urls import path
from main import views

urlpatterns = [
    path('person/', views.person_list),
]