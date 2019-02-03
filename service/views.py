from django.shortcuts import render
from rest_framework.generics import (
	ListAPIView, 
	CreateAPIView , 
	RetrieveAPIView, 
	ListAPIView
	)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User

from .serializers import (
	UserCreateSerializer, 
	UserLoginSerializer,  
)


from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView, 
	CreateAPIView, 
	RetrieveUpdateAPIView, 
	DestroyAPIView
	)


from .models import (
	Category,
	Company, 
	Day, 
	Slot,   
	Address)


from .serializers import (
	CategoryListSerializer,

	CompanyListSerializer,
	CompanyDetailSerializer, 

	SlotListSerializer,
	SlotDetailSerializer,
	SlotCreateSerializer,

	DayDetailSerializer,

	AddressDetailSerializer,
	AddressCreateSerializer,
	AddressListSerializer,


	)

class CategoryListView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategoryListSerializer
	permission_classes = [AllowAny]

class CompanyListView(ListAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyListSerializer
	permission_classes = [AllowAny]

class CompanyDetailView(RetrieveAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanyDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id'
	lookup_url_kwarg = 'company_id'

class DayDetailView(RetrieveAPIView):
	queryset = Day.objects.all()
	serializer_class = DayDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id'
	lookup_url_kwarg = 'day_id'


class SlotUpdateView(RetrieveUpdateAPIView):
	queryset = Slot.objects.all()
	serializer_class = SlotCreateSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id'
	lookup_url_kwarg = 'slot_id'

	def perform_update(self, serializer):
		serializer.save(user = self.request.user)

class SlotListView(ListAPIView):
	serializer_class = SlotListSerializer

	def get_queryset(self):
		user = self.request.user
		return Slot.objects.filter(user = user)

class AddressListView(ListAPIView):
	serializer_class = AddressListSerializer

	def get_queryset(self):
		user = self.request.user
		return Address.objects.filter(user = user)


class AddressDetailView(RetrieveAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressDetailSerializer
	permission_classes = [AllowAny]
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'


class AddressCreateView(CreateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressCreateSerializer
	permission_classes = [IsAuthenticated]
	lookup_field = 'id'
	lookup_url_kwarg = 'address_id'

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

