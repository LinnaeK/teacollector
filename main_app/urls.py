from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teas/', views.teas_index, name='index'),
    path('teas/<int:tea_id>/', views.teas_detail, name='detail'),
    path('teas/create/', views.TeaCreate.as_view(), name='teas_create'),
    path('teas/<int:pk>/update/', views.TeaUpdate.as_view(), name='teas_update'),
    path('teas/<int:pk>/delete/', views.TeaDelete.as_view(), name='teas_delete'),
    path('teas/<int:tea>/add_drinking/', views.add_drinking, name='add_drinking'),
    path('teas/<int:tea_id>/assoc_store/<int:store_id>/', views.assoc_store, name="assoc_store"),
    path('teas/<int:tea_id>/unassoc_store/<int:store_id>/', views.unassoc_store, name="unassoc_store"),
    path('stores/', views.StoreList.as_view(), name='stores_list'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
    path('stores/<int:pk>/', views.StoreDetailView.as_view(), name='store_detail'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup')
]