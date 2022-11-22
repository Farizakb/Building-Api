from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpionts, name='endpoints'),
    path('advocates/', views.advocate_list, name='advocate_list'),
    path('advocates/<str:username>/', views.advocate_detail, name='advocate_detail'),
]
