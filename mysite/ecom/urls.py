from django.urls import path, include
from ecom import views

app_name = 'ecom'

urlpatterns = [

# function based index view
# -------------------------------------------------------------------------------------------------------------------------------------
    path('home/', views.index, name='index'),

# class based index view
# -------------------------------------------------------------------------------------------------------------------------------------
    # path('home/', views.IndexClassView.as_view(), name='index'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    #path('detail/<int:item_id>/', views.detail, name='detail'),

    path('detail/<int:pk>/', views.EcomDetail.as_view(), name='detail'),

    # function based create item view
# -------------------------------------------------------------------------------------------------------------------------------------
#    path('add/', views.create_item, name='create_item'),

    path('add/', views.CreateItem.as_view(), name='create_item' ),


    path('category/<str:val>/',views.category, name="category"),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('update/<int:id>/',views.update_item, name='update_item'),
    path('add-to-cart/', views.add_to_cart, name='addtocart'),
#     path('cart/', views.show_cart, name='showcart'),
]