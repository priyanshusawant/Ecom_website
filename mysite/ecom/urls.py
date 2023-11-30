from django.urls import path, include
from ecom import views

app_name = 'ecom'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:item_id>/', views.detail, name='detail'),
    path('category/<slug:val>/',views.category, name="category"),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]