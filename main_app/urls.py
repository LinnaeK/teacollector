from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teas/', views.teas_index, name='index'),
    path('teas/<int:tea_id>/', views.teas_detail, name='detail'),
    path('teas/create/', views.TeaCreate.as_view(), name='teas_create'),
    path('teas/<int:pk>/update/', views.TeaUpdate.as_view(), name='teas_update'),
    path('teas/<int:pk>/delete/', views.TeaDelete.as_view(), name='teas_delete'),
]