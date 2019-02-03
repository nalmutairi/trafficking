"""trafficking URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from service.views import (
    UserCreateAPIView, 
    UserLoginAPIView, 
    )
from rest_framework_jwt.views import obtain_jwt_token

from service.views import (
    UserCreateAPIView,
    UserLoginAPIView,

    CategoryListView,

    CompanyListView, 
    CompanyDetailView,

    AddressDetailView,
    AddressCreateView,
    AddressListView,
    AddressUpdateView,
    AddressDeleteView,


    DayDetailView,

    SlotListView,
    SlotUpdateView

    )

urlpatterns = [
    path('admin/', admin.site.urls),

    path('category/list/', CategoryListView.as_view(), name = 'category-list'),

    path('company/list/', CompanyListView.as_view(), name ='company-list'),
    path('company/detail/<int:company_id>/', CompanyDetailView.as_view(), name = 'company-detail'),

    path('slot/<int:slot_id>/update/', SlotUpdateView.as_view(), name = 'slot-update'),
    path('slot/list/', SlotListView.as_view(), name = 'slot-list'),

    path('address/detail/<int:address_id>/', AddressDetailView.as_view(), name = 'address-detail'),
    path('address/create/', AddressCreateView.as_view(), name = 'address-create'),
    path('address/list/', AddressListView.as_view(), name = 'address-list'),
    path('address/<int:address_id>/update/', AddressUpdateView.as_view(), name = 'address-update'),
    path('address/<int:address_id>/delete/', AddressDeleteView.as_view(), name = 'address-delete'),

    path('day/detail/<int:day_id>/', DayDetailView.as_view(), name = 'day-detail'),

    path('signup/', UserCreateAPIView.as_view(), name="signup"),
    path('signin/',obtain_jwt_token, name="signin"),
    ]


urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)