from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teas/', views.teas_index, name='index'),
    path('teas/<int:tea_id>/', views.teas_detail, name='detail'),
]