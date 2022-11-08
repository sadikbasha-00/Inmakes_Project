from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='Product_by_Category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='ProdCatdetails'),
]
