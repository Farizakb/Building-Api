from django.urls import path

from . import views 

urlpatterns = [
    path('', views.SearchListOldView.as_view() )
]
