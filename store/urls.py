"""SimpleStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('',views.catalog,name='catalog'),
    path('cart/',views.cart,name='cart'),
    path('cart/remove/',views.removefromcart,name='remove'),
    path('cart/checkout/',views.checkout,name='checkout'),
    path('cart/checkout/complete/',views.completeOrder,name='complete_order'),
    path('admin-login/',views.adminLogin,name='admin_login'),
    path('admin-panel/',views.adminDashboard,name='admin_panel'),
]
