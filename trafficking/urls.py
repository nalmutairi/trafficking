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

# ------- LIST / DETAIL API ---------------
from service.views import (
	CompanyListView, 
	AppointmentListView, 
	CompanyDetailView, 
	DayDetailView, 
	SlotDetailView, 
	AppointmentDetailView,
    CategoryListView,
    ProfileDetailView,
    ProfileCreateView,
    ProfileUpdateView,
    AddressDetailView,
    AddressCreateView,
    AddressUpdateView
	)

# ------- CREATE / UPDATE / DELETE API ----

from service.views import (
	CompanyCreateView,
	DayCreateView,
	SlotCreateView,
	AppointmentCreateView,
	CompanyUpdateView,
	DayUpdateView,
	SlotUpdateView,
	AppointmentUpdateView,
	CompanyDeleteView,

	AppointmentDeleteView
	)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('companylist/', CompanyListView.as_view(), name='companylist'),
    # path('daylist/', DayListView.as_view(), name='daylist'),
    # path('slotlist/', SlotListView.as_view(), name='slotlist'),
    path('appointmentlist/', AppointmentListView.as_view(), name='appointmentlist'),
    path('companydetail/<companydetail_id>', CompanyDetailView.as_view(), name='companydetail'),
    path('daydetail/<daydetail_id>', DayDetailView.as_view(), name='daydetail'),
    path('slotdetail/<slotdetail_id>', SlotDetailView.as_view(), name='slotdetail'),
    path('appointmentdetail/<appointmentdetail_id>', AppointmentDetailView.as_view(), name='appointmentdetail'),
    path('companycreate/', CompanyCreateView.as_view(), name='companycreate'),
    path('daycreate/', DayCreateView.as_view(), name='daycreate'),
    path('slotcreate/', SlotCreateView.as_view(), name='slotcreate'),
    path('appointmentcreate/', AppointmentCreateView.as_view(), name='appointmentcreate'),
    path('companyupdate/<companyupdate_id>', CompanyUpdateView.as_view(), name='companyupdate'),
    path('dayupdate/<dayupdate_id>', DayUpdateView.as_view(), name='dayupdate'),
    path('slotupdate/<slotupdate_id>', SlotUpdateView.as_view(), name='slotupdate'),
    path('appointmentupdate/<appointmentupdate_id>', AppointmentUpdateView.as_view(), name='appointmentupdate'),
    path('companydelete/<companydelete_id>', CompanyDeleteView.as_view(), name='companydelete'),
    # path('daydelete/<daydelete_id>', DayDeleteView.as_view(), name='daydelete'),
    # path('slotdelete/<slotdelete_id>', SlotDeleteView.as_view(), name='slotdelete'),
    path('appointmentdelete/<appointmentdelete_id>', AppointmentDeleteView.as_view(), name='appointmentdelete'),


    path('categorylist', CategoryListView.as_view(), name = 'categorylist'),
    path('profiledetail/<profile_id>', ProfileDetailView.as_view(), name = 'profiledetail'),
    path('profilecreate/', ProfileCreateView.as_view(), name = 'profilecreate'),
    path('profileupdate/<profile_id>', ProfileUpdateView.as_view(), name = 'profileupdate'),

    path('addressdetail/<address_id>', AddressDetailView.as_view(), name = 'addressdetail'),
    path('addressupdate/<address_id>' , AddressUpdateView.as_view(), name = 'addressupdate'),
    path('addresscreate', AddressCreateView.as_view(), name = 'addresscreate'),

    path('signup/', UserCreateAPIView.as_view(), name="signup"),
    path('signin/',obtain_jwt_token, name="signin"),
    # path('user/',UsersListAPIView.as_view(), name="usersList"),
    # path('user_details/<int:user_id>/',UserDetailsAPIView.as_view(), name="userDetail")



]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)