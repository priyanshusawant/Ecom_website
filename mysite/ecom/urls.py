from django.urls import path, include
from ecom import views

app_name = 'ecom'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
]